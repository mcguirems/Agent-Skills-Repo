#!/usr/bin/env python3
"""Normalize simple monochrome SVG icons; preserve geometry and stroke styling."""
import argparse
import copy
import os
from pathlib import Path
import re
import tempfile
import xml.etree.ElementTree as ET
import zipfile

COLORS = ('2DC75C', 'F3D127', 'F32727', 'B0B0B0', 'F2470A', '000069', '555299', '007AFF')
NS = 'http://www.w3.org/2000/svg'
ET.register_namespace('', NS)
SHAPES = {'path', 'rect', 'circle', 'line', 'polyline', 'polygon', 'ellipse'}
PAINT = {'fill', 'stroke', 'color'}
PRESENT = PAINT | {'stroke-width', 'stroke-linecap', 'stroke-linejoin', 'stroke-miterlimit',
                   'stroke-dasharray', 'stroke-dashoffset', 'fill-rule', 'clip-rule',
                   'opacity', 'fill-opacity', 'stroke-opacity', 'vector-effect', 'display', 'visibility'}
INHERITED = PRESENT - {'opacity', 'display', 'vector-effect'}

def local(tag):
    return tag.rsplit('}', 1)[-1]

def declarations(text):
    result = {}
    for part in text.split(';'):
        if not part.strip():
            continue
        if ':' not in part:
            raise ValueError('Invalid CSS declaration')
        key, value = (s.strip() for s in part.split(':', 1))
        if key not in PRESENT or '!important' in value or 'url(' in value.lower():
            raise ValueError('Unsupported CSS property or paint server; review the source artwork')
        result[key] = value
    return result

def read_source(path):
    raw = path.read_text(encoding='utf-8-sig')
    if re.search(r'<!DOCTYPE|<!ENTITY', raw, re.I):
        raise ValueError('DTD/entity declarations are unsupported')
    raw = re.sub(r'<\?xml\b.*?\?>', '', raw, flags=re.S | re.I).strip()
    root = ET.fromstring(raw)
    if local(root.tag) != 'svg' or root.tag not in {'svg', '{'+NS+'}svg'}:
        raise ValueError('Input must be an SVG document')
    if not root.get('viewBox'):
        raise ValueError('An original viewBox is required; cannot infer geometry')
    rules = []
    for node in root.iter():
        if local(node.tag) == 'style':
            text = re.sub(r'/\*.*?\*/', '', node.text or '', flags=re.S)
            matches = list(re.finditer(r'([^{}]+)\{([^{}]*)\}', text))
            if re.sub(r'([^{}]+)\{([^{}]*)\}', '', text).strip():
                raise ValueError('Unsupported CSS syntax')
            for m in matches:
                props = declarations(m.group(2))
                for selector in m.group(1).split(','):
                    selector = selector.strip()
                    if not re.fullmatch(r'\.[A-Za-z_][\w-]*', selector):
                        raise ValueError('Only simple class selectors are supported; review CSS')
                    rules.append((selector[1:], props))
    allowed = SHAPES | {'svg', 'g', 'defs', 'style', 'title', 'desc'}
    computed = {}
    def visit(node, parent):
        kind = local(node.tag)
        if kind not in allowed:
            raise ValueError('Unsupported element '+kind+'; review without altering artwork')
        if kind == 'svg' and node is not root:
            raise ValueError('Nested SVG requires artwork review')
        if any(local(k).startswith('on') for k in node.attrib):
            raise ValueError('Event handlers are unsupported')
        props = {k: v for k, v in parent.items() if k in INHERITED}
        props.update({k: v for k, v in node.attrib.items() if k in PRESENT})
        classes = node.get('class', '').split()
        for klass in classes:
            if not any(c == klass for c, _ in rules):
                raise ValueError('Unresolved CSS class '+klass)
        for klass, rule in rules:
            if klass in classes:
                props.update(rule)
        props.update(declarations(node.get('style', '')))
        if any('url(' in v.lower() for v in props.values()):
            raise ValueError('Paint servers require artwork review')
        computed[node] = props
        for child in node:
            visit(child, props)
    visit(root, {})
    shapes = [n for n in root.iter() if local(n.tag) in SHAPES]
    if not shapes:
        raise ValueError('No drawable icon elements found')
    # SVG defaults: black fill, no stroke. Class CSS and inheritance are resolved first.
    def none(value):
        return value.strip().lower() == 'none'
    outline = sum(none(computed[n].get('fill', 'black')) for n in shapes) > len(shapes)/2
    outline = outline or all('stroke' in computed[n] and 'fill' not in computed[n] for n in shapes)
    if outline:
        if any(not none(computed[n].get('fill', 'none')) for n in shapes):
            raise ValueError('Mixed filled/outline artwork requires review before recoloring')
    elif any(none(computed[n].get('fill', 'black')) or not none(computed[n].get('stroke', 'none'))
             and computed[n].get('stroke-width', '1') not in {'0', '0px'} for n in shapes):
        raise ValueError('Mixed filled/stroked artwork requires review before recoloring')
    result = copy.deepcopy(root)
    # Resolve presentation styling before removing CSS. Preserve geometry attributes everywhere.
    originals = list(root.iter())
    copies = list(result.iter())
    for old, new in zip(originals, copies):
        if local(new.tag) == 'style':
            continue
        for key in list(new.attrib):
            if key in PRESENT or key in {'style', 'class'}:
                del new.attrib[key]
        # Keep non-color rendering properties (including inherited stroke geometry).
        preserve = computed[old]
        for key, value in preserve.items():
            if key not in PAINT:
                new.set(key, value)
        if local(new.tag) in SHAPES:
            new.set('class', 'cls-1')
    for parent in result.iter():
        for child in list(parent):
            if local(child.tag) == 'style':
                parent.remove(child)
    result.set('id', 'Layer_1')
    result.set('data-name', 'Layer 1')
    # Width/height are presentation sizing; viewBox and rendering attributes are preserved.
    result.attrib.pop('width', None)
    result.attrib.pop('height', None)
    for node in result.iter():
        if not node.tag.startswith('{'):
            node.tag = '{'+NS+'}'+node.tag
    defs = next((n for n in result if local(n.tag) == 'defs'), None)
    if defs is None:
        defs = ET.Element('{'+NS+'}defs')
        result.insert(0, defs)
    style = ET.SubElement(defs, '{'+NS+'}style')
    return result, style, 'Outline' if outline else 'Filled'

def convert(input_path, output_dir):
    source = Path(input_path)
    if source.suffix.lower() != '.svg':
        raise ValueError('Input filename must end in .svg')
    name = re.sub(r'-(?:'+ '|'.join(COLORS)+r')$', '', source.stem, flags=re.I)
    if not name or name in {'.', '..'}:
        raise ValueError('Cannot derive icon name; provide a named SVG file')
    root, style, mode = read_source(source)
    output = Path(output_dir)
    output.mkdir(parents=True, exist_ok=True)
    names = [name+'.svg']+[name+'-'+c+'.svg' for c in COLORS]
    # Reject existing targets, so failed writes cannot overwrite a previous conversion.
    targets = names + [name+'.zip']
    if any((output/n).exists() for n in targets):
        raise ValueError('Output files already exist; select a fresh output directory')
    committed = []
    with tempfile.TemporaryDirectory(dir=output) as temporary:
        stage = Path(temporary)
        for filename, color in zip(names, ('000000',)+COLORS):
            if mode == 'Outline':
                style.text = '\n      .cls-1 {\n        fill: none;\n        stroke: #'+color+';\n      }\n    '
            else:
                style.text = '\n      .cls-1 {\n        fill: #'+color+';\n        stroke-width: 0px;\n      }\n    '
            ET.indent(root, space='  ')
            xml = ET.tostring(root, encoding='unicode')
            data = '<?xml version="1.0" encoding="UTF-8"?>\n'+xml+'\n'
            ET.fromstring(data)
            if data.count('<?xml') != 1:
                raise ValueError('XML declaration check failed')
            (stage/filename).write_text(data, encoding='utf-8')
        archive = stage/(name+'.zip')
        with zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED) as z:
            for filename in names:
                z.write(stage/filename, filename)
        with zipfile.ZipFile(archive) as z:
            if z.testzip() is not None or z.namelist() != names or len(z.namelist()) != 9:
                raise ValueError('ZIP verification failed')
        try:
            for filename in targets:
                os.replace(stage/filename, output/filename)
                committed.append(output/filename)
        except BaseException:
            for path in committed:
                path.unlink(missing_ok=True)
            raise
    return output/(name+'.zip'), mode, name

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input_svg', type=Path)
    parser.add_argument('output_directory', type=Path)
    args = parser.parse_args()
    try:
        archive, mode, name = convert(args.input_svg, args.output_directory)
    except (ValueError, OSError, ET.ParseError) as error:
        parser.exit(1, 'Conversion failed: '+str(error)+'\n')
    print(f'{archive}\nType: {mode}\nIcon: {name}')

if __name__ == '__main__':
    main()
