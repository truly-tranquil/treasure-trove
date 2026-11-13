# Compatibility Notes: Zensical Migration (`compat-notes.md`)

## 1. Zensical Build & Compatibility Findings

- **Zensical Version:** `zensical==0.1.1` (with `zensical-ui==0.0.42`).
- **`mkdocs.yml` Parsing:** Zensical successfully reads `mkdocs.yml` as-is, ignoring unsupported MkDocs plugins silently without failing the build.
- **Plugins:**
  - `search`: Built-in or supported natively by Zensical.
  - `awesome-pages`: Ignored by Zensical (Zensical builds navigation based on folder/file structure or explicit `nav:`).
  - `macros`: Zensical natively evaluates Jinja template expressions like `{{ config.extra.contact_url }}` in Markdown files!
  - `git-revision-date-localized`: Ignored by Zensical (footer dates need review or alternative handling).
  - `minify`, `glightbox`, `callouts`, `redirects`, `htmlproofer`, `print-site`: Ignored or handled via built-ins.
- **Overrides:** `overrides/main.html`, `404.html`, and `partials/logo.html` are supported or correctly rendered by Zensical's Material-compatible template structure (Open Graph tags and logo alt text appear correctly).
- **CSS & JS:** `extra.css` and `keyboard.js` function properly with Zensical's DOM output.
- **Base Path & Links:** Resolves correctly under `/treasure-trove/`.
