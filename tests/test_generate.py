"""Tests voor de openbare fictieve demo (geen private data of API's)."""
import copy
import json
import sys
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "demo"))
from generate import generate, to_markdown, STORY_TEMPLATES, match_existing  # noqa: E402


class DemoTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.example = json.loads((ROOT / "demo" / "voorbeeldcontext.json").read_text(encoding="utf-8"))

    def test_example_context_explicitly_fictional(self):
        self.assertIs(self.example["fictief"], True)

    def test_generates_three_complete_stories(self):
        result = generate(self.example)
        self.assertEqual(len(result["stories"]), 3)
        for story in result["stories"]:
            self.assertTrue(story["userstory"].startswith("Als "))
            self.assertIn("zodat ", story["userstory"])
            self.assertTrue(story["business_value"])
            self.assertTrue(story["mvp_value"])
            self.assertEqual(len(story["acceptance_criteria"]), 3)
            self.assertGreaterEqual(len(story["tasks"]), 3)
            for criterion in story["acceptance_criteria"]:
                self.assertIn("Given ", criterion)
                self.assertIn("When ", criterion)
                self.assertIn("Then ", criterion)

    def test_blocks_non_fictional_input(self):
        changed = copy.deepcopy(self.example)
        changed["fictief"] = False
        with self.assertRaises(ValueError):
            generate(changed)

    def test_flags_existing_same_story(self):
        changed = copy.deepcopy(self.example)
        changed["bestaande_backlog"].append({"titel": STORY_TEMPLATES[0]["title"], "status": "Todo"})
        result = generate(changed)
        self.assertEqual(len(result["stories"]), 2)
        self.assertEqual(result["possible_duplicates"][0]["existing"]["status"], "Todo")

    def test_match_existing_returns_none_for_unrelated_title(self):
        self.assertIsNone(match_existing("abc xyz", [{"titel": "iets heel anders", "status": "Done"}]))

    def test_markdown_is_marked_as_example(self):
        text = to_markdown(generate(self.example))
        self.assertIn("FICTIEVE DEMO", text)
        self.assertIn("geen transcript van Copilot", text)
        self.assertIn("MVP-bijdrage", text)

    def test_missing_context_is_rejected(self):
        changed = copy.deepcopy(self.example)
        changed.pop("product_goal")
        with self.assertRaises(ValueError):
            generate(changed)


if __name__ == "__main__":
    unittest.main()
