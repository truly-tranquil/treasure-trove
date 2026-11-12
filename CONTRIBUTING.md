# Contributing to Treasure Trove

Thanks for wanting to help! Treasure Trove is run by one person (Killian / Truly Tranquil) and welcomes volunteers.

## Ways to help

- **Instructional design** — shape courses, sessions, and learning activities.
- **Graphic design** — handouts, slides, and visual assets.
- **Accessibility** — audit pages, PDFs, and color contrast; test with screen readers.
- **Education / tutoring experience** — review course content and handouts.
- **Link maintenance** — the Learning Library and Get Help pages have many external links that need periodic checking.
- **General enthusiasm** — a can-do attitude and 1–3 hours a week go a long way.

## How to contribute

1. Fork the repo and create a branch from `main`.
2. Make your changes to Markdown files in `docs/` (or assets/PDFs).
3. Build locally to verify: `pip install -r requirements.txt && mkdocs build --strict`
4. Open a pull request describing what you changed and why.

## Checking links

Deploys check internal links only, so external sites that block automated
checkers can't stop the site from publishing. A separate **audit external
links** workflow runs every Monday and reports link rot without blocking
deploys. To run the same audit locally, install
[lychee](https://github.com/lycheeverse/lychee) and run:

```bash
lychee --config lychee.toml docs
```

## Code of conduct

Please read and follow [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

## Contact

Reach out via the [official Discord](https://discord.gg/yEWXHNW9gX) or email tranquil.tyrant@gmail.com.