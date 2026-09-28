"""Unit tests for Suspect Notebook UI, Clue Wrapping, Button Styling, and OpenDyslexic metrics."""
import os
import re
import unittest
from pathlib import Path
from PIL import ImageFont

ROOT = Path(__file__).resolve().parents[1]


class SuspectNotebookUITests(unittest.TestCase):
    def setUp(self):
        self.notebook_path = ROOT / "game" / "screens" / "suspect_notebook.rpy"
        self.content = self.notebook_path.read_text(encoding="utf-8")

    def test_notebook_screens_and_modal_properties(self):
        """Verify modal, zorder, background dim, and keyboard bindings."""
        for screen_name in ["suspect_notebook", "suspect_notepad"]:
            self.assertIn(f"screen {screen_name}():", self.content)
            self.assertIn(f'key "game_menu" action Hide("{screen_name}")', self.content)
            self.assertIn(f'key "K_ESCAPE" action Hide("{screen_name}")', self.content)
        self.assertIn("modal True", self.content)
        self.assertIn("zorder 200", self.content)
        self.assertIn('add Solid("#00000099")', self.content)

    def test_button_navigation_and_styling(self):
        """Verify navigation buttons are present and have visual styling."""
        # suspect_notebook buttons
        self.assertIn('textbutton _("Write Notes")', self.content)
        self.assertIn('textbutton _("Close")', self.content)
        self.assertIn('action [Hide("suspect_notebook"), Show("suspect_notepad")]', self.content)

        # suspect_notepad buttons
        self.assertIn('textbutton _("Evidence")', self.content)
        self.assertIn('action [Hide("suspect_notepad"), Show("suspect_notebook")]', self.content)

        # Ensure buttons have styling properties (style, style_prefix, background, or custom style blocks)
        has_styling = (
            "style_prefix" in self.content or 
            "notebook_nav_button" in self.content or 
            "notebook_button" in self.content or 
            "background" in self.content
        )
        self.assertTrue(has_styling, "Notebook buttons must have explicit visual styling")

        # Verify palette colors for theme compliance (#174D60 and #8D3027)
        self.assertIn("#174D60", self.content)
        self.assertIn("#8D3027", self.content)

    def test_suspect_status_differentiation(self):
        """Verify distinct styling for remaining vs cleared suspects."""
        self.assertIn("if suspect_id in remainingSuspects:", self.content)
        self.assertIn("CLEARED", self.content)
        self.assertIn("{s}", self.content)

        # Verify badges and cards
        self.assertIn("suspect_card_active", self.content)
        self.assertIn("suspect_card_cleared", self.content)
        self.assertIn("notebook_badge_active", self.content)
        self.assertIn("notebook_badge_cleared", self.content)
        self.assertIn("[ACTIVE]", self.content)
        self.assertIn("[CLEARED]", self.content)

    def test_clue_text_wrapping_constraints(self):
        """Verify clue text and removed suspect text have xmaximum constraints to prevent overflow."""
        # Find xmaximum constraints on clue text
        matches = re.findall(r'text\s+(?:clue\["text"\]|.*Removed:).*?xmaximum\s+(\d+)', self.content, re.DOTALL)
        self.assertTrue(len(matches) >= 1, "Clue texts must declare xmaximum constraints")
        for xmax in matches:
            self.assertLessEqual(int(xmax), 420, "Clue text xmaximum must not exceed 420px")
            self.assertEqual(int(xmax), 365, "Clue text xmaximum should be 365px to prevent scrollbar collision")

        # Verify clue card styling exists
        self.assertIn("style clue_card:", self.content)

    def test_personal_notes_alignment_and_counter(self):
        """Verify character counter and note input layout in suspect_notepad."""
        self.assertIn("[len(playerInvestigationNotes)]/4000", self.content)
        self.assertIn("VariableInputValue(\"playerInvestigationNotes\")", self.content)
        # Verify right alignment of counter
        self.assertIn("xalign 1.0", self.content)
        # Verify input width constraint
        input_xmax_match = re.search(r'input:.*?xmaximum\s+(\d+)', self.content, re.DOTALL)
        self.assertIsNotNone(input_xmax_match, "Notes input must have xmaximum constraint")
        self.assertLessEqual(int(input_xmax_match.group(1)), 480)

    def test_opendyslexic_compatibility_metrics(self):
        """Verify OpenDyslexic font text fits cleanly inside notebook column boundaries."""
        od_font_path = ROOT / "game" / "fonts" / "OpenDyslexic-Regular.ttf"
        self.assertTrue(od_font_path.is_file(), "OpenDyslexic font file must exist")

        font_suspect = ImageFont.truetype(str(od_font_path), 24)
        font_attrs = ImageFont.truetype(str(od_font_path), 16)

        # Suspect names in OpenDyslexic must fit inside 400px
        names = ["Victor Veytovi", "Jermiah Jones", "Barry Baxter", "Carl Creek", "Tucker Thompson", "Edgar Ebbington", "Simon Streep", "Kyle Kallus", "Alan Ashmore"]
        for name in names:
            bbox = font_suspect.getbbox(name)
            width = bbox[2] - bbox[0]
            self.assertLess(width, 400, f"Suspect name '{name}' exceeds 400px in OpenDyslexic")

        # Cleared suspect attribute line in 16pt must fit inside 405px
        cleared_line = "Light • Average • Brawny (CLEARED)"
        bbox_cleared = font_attrs.getbbox(cleared_line)
        self.assertLess(bbox_cleared[2] - bbox_cleared[0], 405, "Cleared attribute line exceeds 405px")

        # Active attribute line in 16pt must fit inside 365px
        active_line = "Fire • Short • Brawny"
        bbox_active = font_attrs.getbbox(active_line)
        self.assertLess(bbox_active[2] - bbox_active[0], 365, "Active attribute line exceeds 365px")


if __name__ == "__main__":
    unittest.main()
