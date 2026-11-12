"""Validate the MkDocs configuration and navigation structure."""

import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
CONFIG = ROOT / "mkdocs.yml"
DOCS = ROOT / "docs"


class TestMkDocsConfig(unittest.TestCase):
    """Tests for mkdocs.yml and its navigation."""

    @classmethod
    def setUpClass(cls):
        with CONFIG.open(encoding="utf-8") as fh:
            cls.config = yaml.safe_load(fh)

    def test_site_name_is_set(self):
        self.assertIsInstance(self.config.get("site_name"), str)
        self.assertTrue(self.config["site_name"].strip())

    def test_theme_is_material(self):
        theme = self.config.get("theme", {})
        self.assertEqual(theme.get("name"), "material")

    def test_required_plugins_present(self):
        plugins = self.config.get("plugins", [])
        plugin_names = []
        for entry in plugins:
            if isinstance(entry, dict):
                plugin_names.extend(entry.keys())
            else:
                plugin_names.append(entry)
        required = ["search", "minify", "git-revision-date-localized", "awesome-pages"]
        for plugin in required:
            self.assertIn(plugin, plugin_names, f"Missing plugin: {plugin}")

    def test_nav_entries_point_to_existing_files(self):
        """Every file referenced in the top-level nav must exist under docs/."""
        nav = self.config.get("nav", [])
        missing = []

        def walk(items):
            for item in items:
                if isinstance(item, dict):
                    for _title, target in item.items():
                        if isinstance(target, str):
                            path = DOCS / target
                            if not path.exists():
                                missing.append(target)
                        elif isinstance(target, list):
                            walk(target)

        walk(nav)
        self.assertEqual(missing, [], f"Nav references missing files: {missing}")

    def test_docs_directory_exists(self):
        self.assertTrue(DOCS.is_dir(), f"docs directory missing: {DOCS}")


if __name__ == "__main__":
    unittest.main()