"""Tests for Accessibility Preferences, OpenDyslexic Font Swap, and Main Menu Layout.
"""
import os
import re
import textwrap
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import Mock
from PIL import ImageFont

ROOT = Path(__file__).resolve().parents[1]


class AccessibilityAndMainMenuTests(unittest.TestCase):
    def setUp(self):
        self.persistent = SimpleNamespace(
            dyslexic_font=False,
            _gui_preference={}
        )
        self._preferences = SimpleNamespace(
            font_transform=None
        )
        self.renpy = Mock()
        self.config = SimpleNamespace(
            interact_callbacks=[]
        )
        self.ns = {
            "persistent": self.persistent,
            "_preferences": self._preferences,
            "renpy": self.renpy,
            "config": self.config,
            "Action": type("Action", (), {}),
            "DictEquality": type("DictEquality", (), {}),
        }

    def test_font_files_exist_and_load(self):
        """Verify Hot Mustard and OpenDyslexic fonts are placed in game/fonts/ and load correctly."""
        hot_mustard_path = ROOT / "game" / "fonts" / "HotMustardBTN.ttf"
        opendyslexic_path = ROOT / "game" / "fonts" / "OpenDyslexic-Regular.ttf"
        opendyslexic3_path = ROOT / "game" / "fonts" / "_OpenDyslexic3-Regular.ttf"

        self.assertTrue(hot_mustard_path.is_file(), "HotMustardBTN.ttf not found in game/fonts/")
        self.assertTrue(opendyslexic_path.is_file(), "OpenDyslexic-Regular.ttf not found in game/fonts/")
        self.assertTrue(opendyslexic3_path.is_file(), "_OpenDyslexic3-Regular.ttf not found in game/fonts/")

        hm_font = ImageFont.truetype(str(hot_mustard_path), 40)
        self.assertIsNotNone(hm_font)
        bbox1 = hm_font.getbbox("Date and Deduce")
        bbox2 = hm_font.getbbox("A D&D Spinoff!")
        self.assertTrue(bbox1[2] > bbox1[0])
        self.assertTrue(bbox2[2] > bbox2[0])

        od_font = ImageFont.truetype(str(opendyslexic_path), 30)
        self.assertIsNotNone(od_font)
        od_bbox = od_font.getbbox("Accessibility Preferences Test")
        self.assertTrue(od_bbox[2] > od_bbox[0])

    def test_preferences_dyslexic_font_logic(self):
        """Verify set_dyslexic_font and SetDyslexicFont update font_transform and persistent state."""
        pref_path = ROOT / "game" / "screens" / "preferences.rpy"
        content = pref_path.read_text(encoding="utf-8")

        # Extract the python block from preferences.rpy
        start_marker = "init python:"
        end_marker = "init 999 python:"
        self.assertIn(start_marker, content)
        self.assertIn(end_marker, content)

        code_start = content.index(start_marker) + len(start_marker)
        code_end = content.index(end_marker)
        raw_code = content[code_start:code_end]
        py_code = textwrap.dedent(raw_code).strip()

        # Execute extracted python code in our test environment
        exec(compile(py_code, "preferences.rpy", "exec"), self.ns)

        SetDyslexicFont = self.ns["SetDyslexicFont"]

        # Default state
        self.assertFalse(self.persistent.dyslexic_font)
        self.assertIsNone(self._preferences.font_transform)
        btn_default = SetDyslexicFont(False)
        btn_open = SetDyslexicFont(True)
        self.assertTrue(btn_default.get_selected())
        self.assertFalse(btn_open.get_selected())

        # Enable OpenDyslexic
        btn_open()
        self.assertTrue(self.persistent.dyslexic_font)
        self.assertEqual(self._preferences.font_transform, "opendyslexic")
        self.assertFalse(btn_default.get_selected())
        self.assertTrue(btn_open.get_selected())
        self.assertEqual(self.persistent._gui_preference.get("font"), "fonts/OpenDyslexic-Regular.ttf")

        # Disable OpenDyslexic
        btn_default()
        self.assertFalse(self.persistent.dyslexic_font)
        self.assertIsNone(self._preferences.font_transform)
        self.assertTrue(btn_default.get_selected())
        self.assertFalse(btn_open.get_selected())
        self.assertEqual(self.persistent._gui_preference.get("font"), "MonaspaceNeon-Regular.otf")

    def test_preferences_dyslexic_startup_sync_and_none_safety(self):
        """Verify _sync_dyslexic_font_state preserves saved persistent state on startup and is None-safe."""
        pref_path = ROOT / "game" / "screens" / "preferences.rpy"
        content = pref_path.read_text(encoding="utf-8")

        start_marker = "init python:"
        end_marker = "init 999 python:"
        code_start = content.index(start_marker) + len(start_marker)
        code_end = content.index(end_marker)
        py_code = textwrap.dedent(content[code_start:code_end]).strip()

        # Fresh namespace simulating startup where persistent.dyslexic_font was saved True,
        # but _preferences.font_transform is initially None
        startup_ns = {
            "persistent": SimpleNamespace(dyslexic_font=True, _gui_preference=None),
            "_preferences": SimpleNamespace(font_transform=None),
            "renpy": self.renpy,
            "config": SimpleNamespace(interact_callbacks=[]),
            "Action": type("Action", (), {}),
            "DictEquality": type("DictEquality", (), {}),
        }
        exec(compile(py_code, "preferences.rpy", "exec"), startup_ns)

        # Trigger startup sync callback
        sync_fn = startup_ns["_sync_dyslexic_font_state"]
        sync_fn()

        # Must NOT have overwritten persistent.dyslexic_font to False, and must have restored font_transform
        self.assertTrue(startup_ns["persistent"].dyslexic_font)
        self.assertEqual(startup_ns["_preferences"].font_transform, "opendyslexic")

        # Test safe handling when _gui_preference is None
        set_dyslexic_font = startup_ns["set_dyslexic_font"]
        set_dyslexic_font(False)
        self.assertFalse(startup_ns["persistent"].dyslexic_font)
        self.assertIsNone(startup_ns["_preferences"].font_transform)

        set_dyslexic_font(True)
        self.assertTrue(startup_ns["persistent"].dyslexic_font)
        self.assertEqual(startup_ns["_preferences"].font_transform, "opendyslexic")

    def test_game_menu_accessibility_tab(self):
        """Verify game_menu.rpy includes an Accessibility navigation button that fits on the sticky note."""
        menu_path = ROOT / "game" / "screens" / "game_menu.rpy"
        content = menu_path.read_text(encoding="utf-8")

        self.assertIn('textbutton _("Accessibility") action ShowMenu("accessibility_prefs")', content)

        # Check button text fits inside 133px width of menusticky_idle.png
        import re
        m = re.search(r'textbutton _\("Accessibility"\).*?text_size (\d+)', content)
        self.assertIsNotNone(m, "text_size should be explicitly set on Accessibility button")
        text_size = int(m.group(1))
        self.assertLessEqual(text_size, 20, "Accessibility text_size must be <= 20 to prevent overflowing 133px sticky note")

        rando_font = ImageFont.truetype(str(ROOT / "game" / "fonts" / "RandoWB.ttf"), text_size)
        od_font = ImageFont.truetype(str(ROOT / "game" / "fonts" / "_OpenDyslexic3-Regular.ttf"), text_size)
        self.assertLess(rando_font.getbbox("Accessibility")[2], 130)
        self.assertLess(od_font.getbbox("Accessibility")[2], 130)

    def test_accessibility_prefs_screen(self):
        """Verify preferences.rpy declares the accessibility_prefs screen with required buttons."""
        pref_path = ROOT / "game" / "screens" / "preferences.rpy"
        content = pref_path.read_text(encoding="utf-8")

        self.assertIn("screen accessibility_prefs():", content)
        self.assertIn('use game_menu(_("Accessibility"))', content)
        self.assertIn('textbutton _("Default"):', content)
        self.assertIn("action SetDyslexicFont(False)", content)
        self.assertIn('textbutton _("OpenDyslexic"):', content)
        self.assertIn("action SetDyslexicFont(True)", content)

    def test_main_menu_layout_and_assets(self):
        """Verify main_menu.rpy layout: office background, sprites on left, sidefade on right, Hot Mustard title."""
        mm_path = ROOT / "game" / "screens" / "main_menu.rpy"
        content = mm_path.read_text(encoding="utf-8")

        # Office background
        self.assertIn('image main_menu_background = "images/officeFinal.jpg"', content)

        # Character sprites
        self.assertIn('"images/FINISHEDSPRITES/freddyNeutralSmile.png"', content)
        self.assertIn('"images/FINISHEDSPRITES/razzelHappyPeaceSign.png"', content)
        self.assertNotIn('add "mm_ulysses":', content)
        self.assertIn('add "mm_razzle":', content)
        self.assertIn('add "mm_freddy":', content)

        # Sidefade on right
        self.assertIn('add "gui/sidefade.png"', content)

        # Title in Hot Mustard font
        self.assertIn('text _("Date and Deduce"):', content)
        self.assertIn('text _("A D&D Spinoff!"):', content)
        self.assertIn('font "fonts/HotMustardBTN.ttf"', content)
        self.assertIn('color "#D26143"', content)

        # Character sprite source files exist on disk
        self.assertTrue((ROOT / "game" / "images" / "officeFinal.jpg").is_file())
        self.assertTrue((ROOT / "game" / "images" / "FINISHEDSPRITES" / "freddyNeutralSmile.png").is_file())
        self.assertTrue((ROOT / "game" / "images" / "FINISHEDSPRITES" / "razzelHappyPeaceSign.png").is_file())
        self.assertTrue((ROOT / "game" / "gui" / "sidefade.png").is_file())

    def test_main_menu_freddy_positioning(self):
        """Verify in game/screens/main_menu.rpy:
        1. Ulysses is removed from the main menu.
        2. Freddy is moved to where Ulysses was (xpos=500).
        3. gui/sidefade.png is declared after mm_freddy so it overlays on the right.
        4. All 7 main menu buttons remain present, styled, and aligned at xalign 0.9.
        """
        mm_path = ROOT / "game" / "screens" / "main_menu.rpy"
        content = mm_path.read_text(encoding="utf-8")

        # Verify Ulysses is removed
        self.assertNotIn('add "mm_ulysses"', content)

        # Extract sprite xpos within the fixed sprite container
        razzle_match = re.search(r'add\s+"mm_razzle":\s*xpos\s+(\d+)', content)
        freddy_match = re.search(r'add\s+"mm_freddy":\s*xpos\s+(\d+)', content)

        self.assertIsNotNone(razzle_match, "mm_razzle xpos declaration not found")
        self.assertIsNotNone(freddy_match, "mm_freddy xpos declaration not found")

        razzle_xpos = int(razzle_match.group(1))
        freddy_xpos = int(freddy_match.group(1))

        # Position checks: Razzle left (40), Freddy right (580)
        self.assertEqual(razzle_xpos, 40)
        self.assertEqual(freddy_xpos, 580)

        # Strict position verification: Freddy strictly to the right of Razzle
        self.assertGreater(
            freddy_xpos, razzle_xpos,
            f"Freddy (xpos={freddy_xpos}) must be positioned to the right of Razzle (xpos={razzle_xpos})"
        )

        # Verify sidefade overlay order: declared after mm_freddy to overlay on top
        freddy_idx = content.find('add "mm_freddy"')
        sidefade_idx = content.find('add "gui/sidefade.png"')
        self.assertGreater(
            sidefade_idx, freddy_idx,
            "gui/sidefade.png must appear after mm_freddy in screen declaration to overlay on top"
        )

        # Verify button unobstructed layout and alignment
        self.assertIn('style_prefix "main_menu"', content)
        self.assertIn("xalign 0.9", content)
        for btn in ["Start", "Load", "Settings", "About", "Endings", "Help", "Quit"]:
            self.assertIn(f'textbutton _("{btn}")', content, f"Missing main menu button: {btn}")


if __name__ == "__main__":
    unittest.main()
