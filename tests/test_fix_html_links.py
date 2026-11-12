import tempfile
import unittest
from pathlib import Path

from scripts.fix_html_links import fix_html_links


class TestFixHtmlLinks(unittest.TestCase):
    def test_normalizes_single_backslashes_in_html_links(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            site = Path(temp_dir)
            page = site / "index.html"
            page.write_text(r'<a href="docs\page.html"></a>', encoding="utf-8")

            fixed = fix_html_links(site)

            self.assertEqual(fixed, 1)
            self.assertEqual(
                page.read_text(encoding="utf-8"),
                '<a href="docs/page.html"></a>',
            )


if __name__ == "__main__":
    unittest.main()
