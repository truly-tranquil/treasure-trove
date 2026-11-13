# Baseline Notes (MkDocs Build)

- **Total Page Count (`index.html` files):** 37
- **Required Files Present:**
  - `sitemap.xml` (Present, size 6,108 bytes)
  - `search/search_index.json` (Present)
  - `robots.txt` (Present, size 93 bytes)
  - `404.html` (Present)
  - `print_page/index.html` (Present)
- **Navigation Tree:** Rendered correctly via `awesome-pages` plugin into a hierarchical menu matching the `.pages` definitions across courses, modules, and supplementary pages (Get Help, Learning Library, What's Next, Meet the Team).
- **Macro Verification:** `{{ config.extra.contact_url }}` evaluated correctly to `https://linktr.ee/truly.tranquil` on the course index and syllabus pages.
- **Open Graph Tags:** Present on home page and inner pages, generated via `overrides/main.html`.
- **Footer Last Updated:** Git revision date localized plugin populated footer modification timestamps correctly.
- **Reference Page:** `reference-page.md` was not present in the repository root; baseline build completed successfully for all existing `docs/` content.
