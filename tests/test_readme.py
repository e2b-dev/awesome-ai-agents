import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from check_readme import validate_readme_text  # noqa: E402


class ReadmeIntegrityTests(unittest.TestCase):
    def test_repository_readme_passes(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertEqual(validate_readme_text(readme), [])

    def test_detects_malformed_markdown_url_and_empty_list_item(self):
        readme = (
            "## [Example](https://example.com)\n"
            "- [Broken](https:example.com)\n"
            "- \n"
        )
        issues = validate_readme_text(readme)
        self.assertTrue(any("missing //" in issue for issue in issues))
        self.assertTrue(any("empty list item" in issue for issue in issues))

    def test_detects_duplicate_project_name_and_url(self):
        readme = (
            "## [Example](https://example.com)\n"
            "## [Example](https://example.com/)\n"
        )
        issues = validate_readme_text(readme)
        self.assertTrue(any("duplicate project name" in issue for issue in issues))
        self.assertTrue(any("duplicate project URL" in issue for issue in issues))

    def test_detects_repeated_category_section(self):
        readme = (
            "## [Example](https://example.com)\n"
            "### Category\nGeneral\n"
            "### Category\nProductivity\n"
        )
        self.assertTrue(
            any("repeats its Category section" in issue for issue in validate_readme_text(readme))
        )

    def test_detects_unmatched_details_tags_but_ignores_comments_and_fences(self):
        valid = (
            "<!-- </details> -->\n"
            "```html\n<details>\n````\n"
            "<details>\ncontent\n</details>\n"
        )
        self.assertEqual(validate_readme_text(valid), [])
        self.assertTrue(
            any(
                "unmatched </details>" in issue
                for issue in validate_readme_text("</details>\n")
            )
        )
        self.assertTrue(
            any(
                "is not closed" in issue
                for issue in validate_readme_text("<details>\n")
            )
        )


if __name__ == "__main__":
    unittest.main()
