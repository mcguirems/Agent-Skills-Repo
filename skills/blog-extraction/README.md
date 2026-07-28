# Blog Extraction

`blog-extraction` packages a repeatable workflow for converting an article, blog post, or uploaded document into two markdown outputs:

- a clean full-text extraction
- a concise coaching or reference summary

The packaged version is portable for Codex and other agent environments because it avoids hardcoded local paths and runtime-specific tool names.

## Included files

- `SKILL.md`
- `README.md`
- `Install-this-skill.md`
- `references/output-templates.md`
- `source/blog-extraction-SKILL_CLAUDE.md`
- `source/blog-extraction_CLAUDE.skill`

## Packaging notes

The original source instructions used a different runtime with tools like `web_fetch`, `bash_tool`, and `present_files`, plus fixed `/mnt/user-data/...` paths. The packaged skill converts those assumptions into portable instructions for the current runtime.
