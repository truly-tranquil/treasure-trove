"""Fix Windows-style backslash path separators in built HTML links.

Run after `mkdocs build`:

    python scripts/fix_html_links.py
"""
from pathlib import Path
import re

SITE = Path('site')

# Match href="..." or src="..." attributes containing a backslash
ATTR_RE = re.compile(r'(href|src)="([^"]*\\[^"]*)"')

def fix_html_links(site: Path = SITE) -> int:
    fixed = 0
    for html in site.rglob('*.html'):
        content = html.read_text(encoding='utf-8')
        new_content, count = ATTR_RE.subn(
            lambda m: f'{m.group(1)}="{m.group(2).replace(chr(92), "/")}"',
            content,
        )
        if count:
            html.write_text(new_content, encoding='utf-8')
            fixed += count
            print(f'Fixed {count} link(s) in {html.relative_to(site)}')

    print(f'Total: {fixed} link(s) fixed across {site}')
    return fixed


if __name__ == '__main__':
    fix_html_links()