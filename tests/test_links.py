"""Validate that internal links in Markdown files resolve to existing files."""

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"

# Matches [text](target.md) or [text](target.md#anchor), capturing the path.
INTERNAL_LINK = re.compile(r"\[[^\]]*\]\(([^)]+\.md(?:#.*)?)\)")


def iter_markdown_files():
    for path in DOCS.rglob("*.md"):
        yield path


class TestInternalLinks(unittest.TestCase):
    """Tests that every internal Markdown link points to a real file."""

    def test_all_internal_links_resolve(self):
        broken = []
        for md_file in iter_markdown_files():
            source = md_file.read_text(encoding="utf-8")
            base_dir = md_file.parent
            for match in INTERNAL_LINK.finditer(source):
                target = match.group(1).split("#", 1)[0]
                # Resolve relative to the source file's directory.
                candidate = (base_dir / target).resolve()
                if not candidate.exists():
                    broken.append(f"{md_file.relative_to(ROOT)} -> {target}")
        self.assertEqual(
            broken,
            [],
            f"Broken internal links found:\n" + "\n".join(broken),
        )


if __name__ == "__main__":
    unittest.main()