"""Regression tests for the public-issue-driven aquarium renderer."""
import importlib.util
import unittest
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("aquarium", ROOT / "update_aquarium.py")
aquarium = importlib.util.module_from_spec(spec)
spec.loader.exec_module(aquarium)


def event(choice="Feed the betta", number=10, title="[Aquarium] test"):
    return {"action": "opened", "issue": {
        "number": number, "title": title,
        "body": "### Action\n\n" + choice + "\n"
    }}


def state():
    return {"feed_count": 0, "lighting": "daylight",
            "last_action": "", "last_issue": 0}


class AquariumTests(unittest.TestCase):
    def test_feed_and_duplicate(self):
        s = state()
        self.assertTrue(aquarium.update(event(), s))
        self.assertEqual(s["feed_count"], 1)
        self.assertFalse(aquarium.update(event(), s))
        self.assertEqual(s["feed_count"], 1)

    def test_unrelated_issue_ignored(self):
        s = state()
        self.assertFalse(aquarium.update(event(title="README typo"), s))
        self.assertFalse(aquarium.update({"action": "closed", "issue": event()["issue"]}, s))
        self.assertEqual(s, state())

    def test_reject_arbitrary_input(self):
        s = state()
        self.assertFalse(aquarium.update(event("Feed the betta; rm -rf /"), s))
        self.assertFalse(aquarium.update(event("<script>alert(1)</script>"), s))
        self.assertEqual(s, state())

    def test_light_controls(self):
        s = state()
        self.assertTrue(aquarium.update(event("Turn on moonlight", 11), s))
        self.assertEqual(s["lighting"], "moonlight")
        self.assertTrue(aquarium.update(event("Turn on daylight", 12), s))
        self.assertEqual(s["lighting"], "daylight")

    def test_render_is_valid_and_idempotent(self):
        svg = (ROOT / "assets" / "readme-terrarium.svg").read_text()
        s = state()
        aquarium.update(event("Turn on moonlight"), s)
        first = aquarium.render(svg, s)
        second = aquarium.render(first, s)
        self.assertEqual(first, second)
        self.assertEqual(second.count('<g id="habitat-state">'), 1)
        self.assertIn("MOONLIGHT", first)
        self.assertIn("SNACKS: 0", first)
        ET.fromstring(first)


if __name__ == "__main__":
    unittest.main()
