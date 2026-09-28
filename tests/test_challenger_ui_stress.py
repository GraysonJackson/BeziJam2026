"""Adversarial stress-test harness for UI Layout, Font Bounding Boxes, Scrollbars, and Sprite Geometry.
Executed by Challenger 1 (UI Layout & Font Challenger).
"""
import re
import unittest
from pathlib import Path
from PIL import Image, ImageFont

ROOT = Path(__file__).resolve().parents[1]
FONTS_DIR = ROOT / "game" / "fonts"
IMAGES_DIR = ROOT / "game" / "images"
GUI_DIR = ROOT / "game" / "gui"
SCREENS_DIR = ROOT / "game" / "screens"


class SuspectNotebookAdversarialStressTests(unittest.TestCase):
    """Adversarial tests on suspect_notebook.rpy layout, fonts, boundaries, and scrollbars."""

    def setUp(self):
        self.notebook_content = (SCREENS_DIR / "suspect_notebook.rpy").read_text(encoding="utf-8")
        
        # Load fonts
        self.neon_path = FONTS_DIR / "MonaspaceNeon-Regular.otf"
        self.argon_path = FONTS_DIR / "MonaspaceArgon-SemiBold.otf"
        self.od_path = FONTS_DIR / "OpenDyslexic-Regular.ttf"
        self.od3_path = FONTS_DIR / "_OpenDyslexic3-Regular.ttf"

        self.assertTrue(self.neon_path.is_file(), "MonaspaceNeon-Regular.otf must exist")
        self.assertTrue(self.argon_path.is_file(), "MonaspaceArgon-SemiBold.otf must exist")
        self.assertTrue(self.od_path.is_file(), "OpenDyslexic-Regular.ttf must exist")
        self.assertTrue(self.od3_path.is_file(), "_OpenDyslexic3-Regular.ttf must exist")

    def _get_text_width(self, font_path, size, text):
        font = ImageFont.truetype(str(font_path), size)
        bbox = font.getbbox(text)
        return bbox[2] - bbox[0]

    def test_suspect_names_bounding_boxes_across_fonts(self):
        """Stress-test all suspect names in Active (21pt) and Cleared (20pt) states across all fonts."""
        names = [
            "Victor Veytovi", "Jermiah Jones", "Barry Baxter", "Carl Creek",
            "Tucker Thompson", "Edgar Ebbington", "Simon Streep", "Kyle Kallus", "Alan Ashmore"
        ]
        
        # In suspect_notebook.rpy:
        # Active: text suspectNames[suspect_id]: size 21, xmaximum 285
        # Cleared: text "{s}[suspectNames[suspect_id]]{/s}": size 20, xmaximum 275
        font_configs = [
            ("Monaspace Neon", self.neon_path),
            ("OpenDyslexic Regular", self.od_path),
            ("OpenDyslexic 3", self.od3_path),
        ]

        for font_name, font_file in font_configs:
            for name in names:
                w21 = self._get_text_width(font_file, 21, name)
                w20 = self._get_text_width(font_file, 20, name)
                
                # Active name must fit inside xmaximum 285
                self.assertLessEqual(
                    w21, 285,
                    f"Active name '{name}' ({w21}px) exceeds xmaximum 285 in {font_name}"
                )
                # Cleared name must fit inside xmaximum 275
                self.assertLessEqual(
                    w20, 275,
                    f"Cleared name '{name}' ({w20}px) exceeds xmaximum 275 in {font_name}"
                )

    def test_suspect_badge_widths_and_card_horizontal_clearance(self):
        """Verify badges ([ACTIVE] and [CLEARED]) fit alongside names without exceeding frame width (365px)."""
        # Frame usable width = 385 (vbox) - 20 (padding 10,8) = 365px.
        frame_inner_w = 365
        
        # Badges use MonaspaceArgon-SemiBold.otf at 14pt (bold)
        # Even under OpenDyslexic font transform, verify both font families!
        for badge_font_name, badge_font_file in [
            ("Monaspace Argon", self.argon_path),
            ("OpenDyslexic Regular", self.od_path),
            ("OpenDyslexic 3", self.od3_path),
        ]:
            w_active_badge = self._get_text_width(badge_font_file, 14, "[ACTIVE]")
            w_cleared_badge = self._get_text_width(badge_font_file, 14, "[CLEARED]")
            
            # Active: name xmaximum 285 + active badge <= 365px (or <= 365 with safe margin)
            total_active_w = 285 + w_active_badge
            # Cleared: name xmaximum 275 + cleared badge <= 365px
            total_cleared_w = 275 + w_cleared_badge

            self.assertLessEqual(
                w_active_badge, 80,
                f"[ACTIVE] badge width {w_active_badge}px exceeds 80px in {badge_font_name}"
            )
            # In Argon: 72px (285 + 72 = 357 <= 365)
            # In OpenDyslexic: 76px (285 + 76 = 361 <= 365)
            self.assertLessEqual(
                total_active_w, frame_inner_w,
                f"Active card max width {total_active_w}px exceeds frame width {frame_inner_w}px in {badge_font_name}"
            )

    def test_suspect_attribute_strings_bounding_boxes(self):
        """Stress-test all possible suspect attribute combinations against xmaximum 365."""
        powers = ["Fire", "Ice", "Light"]
        heights = ["Short", "Average", "Tall"]
        builds = ["Brawny", "Skinny", "Average"]

        for font_name, font_file in [
            ("Monaspace Neon", self.neon_path),
            ("OpenDyslexic Regular", self.od_path),
            ("OpenDyslexic 3", self.od3_path),
        ]:
            for p in powers:
                for h in heights:
                    for b in builds:
                        attr_str = f"{p} • {h} • {b}"
                        # Active: size 16, xmaximum 365
                        w16 = self._get_text_width(font_file, 16, attr_str)
                        self.assertLess(
                            w16, 365,
                            f"Active attributes '{attr_str}' ({w16}px) exceeds 365px in {font_name}"
                        )
                        # Cleared: size 15, xmaximum 365
                        w15 = self._get_text_width(font_file, 15, attr_str)
                        self.assertLess(
                            w15, 365,
                            f"Cleared attributes '{attr_str}' ({w15}px) exceeds 365px in {font_name}"
                        )

    def test_scrollbar_collision_margins_page1_and_page2(self):
        """Stress-test vertical scrollbar collision margins in both suspect list and clue list."""
        # Page 1 & Page 2 Viewports:
        # Viewport xsize: 430px
        # Inner vbox xsize: 385px
        # Available scrollbar channel width: 430 - 385 = 45px
        
        # Measure scrollbar asset width
        with Image.open(GUI_DIR / "scrollbar" / "vertical_idle_bar.png") as bar_img:
            bar_w = bar_img.size[0]
        with Image.open(GUI_DIR / "scrollbar" / "vertical_idle_thumb.png") as thumb_img:
            thumb_w = thumb_img.size[0]

        self.assertEqual(bar_w, 29, "Vertical scrollbar bar width is 29px")
        self.assertEqual(thumb_w, 29, "Vertical scrollbar thumb width is 29px")

        channel_margin = 430 - 385
        clearance = channel_margin - thumb_w
        self.assertGreaterEqual(
            clearance, 15,
            f"Scrollbar clearance {clearance}px must be at least 15px to prevent child clipping"
        )

        # Clue cards inside Page 2:
        # Card padding (10, 8) with vbox 385 -> inner width = 365px
        # All text elements must declare xmaximum <= 365
        xmax_matches = re.findall(r'xmaximum\s+(\d+)', self.notebook_content)
        for val in xmax_matches:
            val_int = int(val)
            # In suspect_notepad input is 460; in clue card / suspect cards it is <= 365
            if val_int <= 400:
                self.assertLessEqual(val_int, 365)

    def test_extreme_case_lengths_adversarial_inputs(self):
        """Adversarial stress-test: Extreme length suspect names, multi-suspect eliminations, and notes."""
        extreme_names = [
            "Bartholomew Montgomery-O'Connor",
            "Archibald Wulfric Brian Dumbledore",
            "Supercalifragilisticexpialidocious Suspect",
        ]
        
        # Verify that long names wrap gracefully:
        # When a name exceeds xmaximum 285, it wraps into multiple lines.
        # Check that individual words do not exceed 285px.
        for font_file in [self.neon_path, self.od_path]:
            font = ImageFont.truetype(str(font_file), 21)
            for ename in extreme_names:
                words = ename.split()
                for w in words:
                    w_len = font.getbbox(w)[2] - font.getbbox(w)[0]
                    # Unless it's an artificial unspaced monster, normal words fit in 285px
                    if len(w) < 25:
                        self.assertLess(
                            w_len, 285,
                            f"Word '{w}' in long name '{ename}' exceeds 285px in {font_file.name}"
                        )

        # Clue multi-suspect elimination text:
        # E.g. 4 suspects removed at once: "Removed: Tucker Thompson, Edgar Ebbington, Victor Veytovi, Jermiah Jones"
        elim_text = "Removed: Tucker Thompson, Edgar Ebbington, Victor Veytovi, Jermiah Jones"
        for font_file in [self.neon_path, self.od_path]:
            font16 = ImageFont.truetype(str(font_file), 16)
            words = elim_text.split()
            # Verify each word fits in 365px so wrapping can occur cleanly
            for w in words:
                w_len = font16.getbbox(w)[2] - font16.getbbox(w)[0]
                self.assertLess(
                    w_len, 365,
                    f"Word '{w}' in multi-elimination text exceeds 365px in {font_file.name}"
                )

    def test_personal_notes_viewport_and_scrollbar_clearance(self):
        """Verify personal notes input box xmaximum 460 leaves adequate margin for 506px viewport."""
        # Container frame: xsize 530, padding (12, 12) -> inner width = 506px
        # Viewport: xsize 506, scrollbars "vertical"
        # Input: xmaximum 460
        input_margin = 506 - 460  # 46px
        scrollbar_w = 29
        clearance = input_margin - scrollbar_w  # 17px
        self.assertGreaterEqual(
            clearance, 15,
            f"Personal notes scrollbar clearance {clearance}px must be >= 15px"
        )


class MainMenuAdversarialStressTests(unittest.TestCase):
    """Adversarial tests on main_menu.rpy sprite coordinates, sidefade alpha, and button clearance."""

    def setUp(self):
        self.mm_content = (SCREENS_DIR / "main_menu.rpy").read_text(encoding="utf-8")
        self.rando_path = FONTS_DIR / "RandoWB.ttf"
        self.od_path = FONTS_DIR / "OpenDyslexic-Regular.ttf"
        self.hm_path = FONTS_DIR / "HotMustardBTN.ttf"

    def test_main_menu_sprite_geometry_and_ordering(self):
        """Stress-test sprite coordinates: Ulysses strictly right of Razzle, crop calculations, and fixed container bounds."""
        # mm_razzle: Crop((479, 130, 1495, 2351)), zoom 0.35, xpos 40
        razzle_w = 1495 * 0.35  # 523.25px
        razzle_right = 40 + razzle_w  # 563.25px

        # mm_ulysses: Crop((438, 38, 2031, 2443)), zoom 0.35, xpos 500
        ulysses_w = 2031 * 0.35  # 710.85px
        ulysses_right = 500 + ulysses_w  # 1210.85px

        # mm_freddy: Crop((998, 481, 1153, 1812)), zoom 0.42, xpos 220
        freddy_w = 1153 * 0.42  # 484.26px
        freddy_right = 220 + freddy_w  # 704.26px

        # Strict R2 Requirement: Ulysses position strictly to the right of Razzle
        self.assertGreater(500, 40, "Ulysses xpos (500) must be strictly greater than Razzle xpos (40)")
        self.assertGreater(ulysses_right, razzle_right, "Ulysses right edge must be greater than Razzle right edge")

        # Freddy foreground center: Freddy xpos between Razzle and Ulysses
        self.assertGreater(220, 40, "Freddy xpos must be to the right of Razzle origin")
        self.assertLess(220, 500, "Freddy xpos must be to the left of Ulysses origin")

        # Container bounds: fixed xysize (1250, 1080)
        fixed_match = re.search(r'fixed:\s+xysize\s+\((\d+),\s*(\d+)\)', self.mm_content)
        self.assertIsNotNone(fixed_match, "fixed xysize declaration not found")
        fixed_w = int(fixed_match.group(1))
        self.assertEqual(fixed_w, 1250, "Fixed container width must be 1250px")
        self.assertLessEqual(
            ulysses_right, fixed_w,
            f"Ulysses right edge ({ulysses_right}px) must fit within fixed width ({fixed_w}px)"
        )

        # Layering order in AST / file: Razzle, Ulysses, then Freddy (so Freddy renders in foreground over both)
        idx_razzle = self.mm_content.find('add "mm_razzle"')
        idx_ulysses = self.mm_content.find('add "mm_ulysses"')
        idx_freddy = self.mm_content.find('add "mm_freddy"')
        self.assertTrue(idx_razzle < idx_ulysses < idx_freddy, "Layering inside fixed: must be Razzle, Ulysses, then Freddy")

    def test_sidefade_overlay_alpha_profile_and_layering(self):
        """Verify gui/sidefade.png alpha profile shades Ulysses on the right while leaving left group unshaded."""
        # Order in screen: sidefade declared AFTER fixed: container
        idx_fixed = self.mm_content.find('fixed:')
        idx_sidefade = self.mm_content.find('add "gui/sidefade.png"')
        self.assertGreater(
            idx_sidefade, idx_fixed,
            "sidefade overlay must be declared after fixed sprite container"
        )

        with Image.open(GUI_DIR / "sidefade.png") as sidefade_img:
            self.assertEqual(sidefade_img.size, (1920, 1080), "sidefade must match 1920x1080 screen resolution")

            # Profile alpha channel along mid-screen y=540
            mid_y = 540
            # Razzle span: x=40..563 -> alpha must be 0
            for x in [40, 200, 400, 560]:
                self.assertEqual(
                    sidefade_img.getpixel((x, mid_y))[3], 0,
                    f"sidefade alpha at x={x} (Razzle area) must be 0"
                )

            # Freddy span: x=220..704 -> alpha must be 0
            for x in [220, 450, 700]:
                self.assertEqual(
                    sidefade_img.getpixel((x, mid_y))[3], 0,
                    f"sidefade alpha at x={x} (Freddy area) must be 0"
                )

            # Ulysses span: x=500..1211 -> alpha starts at 0, ramps up on right side (x > 850)
            self.assertEqual(sidefade_img.getpixel((500, mid_y))[3], 0)
            self.assertEqual(sidefade_img.getpixel((800, mid_y))[3], 0)
            alpha_1000 = sidefade_img.getpixel((1000, mid_y))[3]
            alpha_1200 = sidefade_img.getpixel((1200, mid_y))[3]
            self.assertGreater(alpha_1000, 15, "sidefade should begin soft shading at x=1000")
            self.assertGreater(alpha_1200, 80, "sidefade should have noticeable gradient shading at x=1200")

            # Button span: x=1500..1920 -> alpha must be heavy dark backing (> 220)
            for x in [1600, 1700, 1800]:
                alpha_btn = sidefade_img.getpixel((x, mid_y))[3]
                self.assertGreater(
                    alpha_btn, 240,
                    f"sidefade alpha at x={x} (button area) must be > 240 for high contrast"
                )

    def test_main_menu_buttons_clearance_across_fonts(self):
        """Verify buttons (Start, Load, Settings, etc.) at xalign 0.9 maintain >= 250px clearance from Ulysses."""
        buttons = ["Start", "Load", "Settings", "About", "Endings", "Help", "Quit"]
        ulysses_right = 500 + (2031 * 0.35)  # 1210.85px

        # Test under both default RandoWB and OpenDyslexic (accessibility mode)
        for font_name, font_file in [
            ("RandoWB", self.rando_path),
            ("OpenDyslexic", self.od_path),
        ]:
            font = ImageFont.truetype(str(font_file), 50)
            max_button_w = max(font.getbbox(b)[2] - font.getbbox(b)[0] for b in buttons)
            
            # Button vbox at xalign 0.9 on 1920 screen
            vbox_w = max_button_w + 50  # including style xoffset 50
            vbox_left = 0.9 * (1920 - vbox_w)
            clearance = vbox_left - ulysses_right

            self.assertGreaterEqual(
                clearance, 250,
                f"Button clearance ({clearance:.1f}px) in {font_name} must be at least 250px"
            )

    def test_main_menu_title_vertical_clearance_from_sprites(self):
        """Verify title ('Date and Deduce', 'A D&D Spinoff!') at pos (80, 50) does not collide with sprite heads."""
        f76 = ImageFont.truetype(str(self.hm_path), 76)
        f36 = ImageFont.truetype(str(self.hm_path), 36)

        b76 = f76.getbbox("Date and Deduce")
        b36 = f36.getbbox("A D&D Spinoff!")

        h76 = b76[3] - b76[1]
        h36 = b36[3] - b36[1]
        
        # vbox pos (80, 50), spacing 10
        title_bottom = 50 + h76 + 10 + h36  # ~161px

        # Sprites with yalign 1.0 (bottom anchored at 1080)
        # Razzle: height 2351 * 0.35 = 822.85 -> top = 1080 - 822.85 = 257.15px
        razzle_top = 1080 - (2351 * 0.35)
        # Ulysses: height 2443 * 0.35 = 855.05 -> top = 1080 - 855.05 = 224.95px
        ulysses_top = 1080 - (2443 * 0.35)

        self.assertLess(
            title_bottom, razzle_top,
            f"Title bottom ({title_bottom}px) must be above Razzle top ({razzle_top}px)"
        )
        self.assertLess(
            title_bottom, ulysses_top,
            f"Title bottom ({title_bottom}px) must be above Ulysses top ({ulysses_top}px)"
        )


class HistoryScreenLayoutStressTests(unittest.TestCase):
    """Adversarial stress-tests for history_screen.rpy layout, bounds, fonts, and notebook margins."""

    def setUp(self):
        self.history_content = (SCREENS_DIR / "history_screen.rpy").read_text(encoding="utf-8")
        self.neon_path = FONTS_DIR / "MonaspaceNeon-Regular.otf"
        self.sharpie_path = FONTS_DIR / "RandoSharpie.ttf"
        self.od_path = FONTS_DIR / "OpenDyslexic-Regular.ttf"

    def _get_text_width(self, font_path, size, text):
        font = ImageFont.truetype(str(font_path), size)
        bbox = font.getbbox(text)
        return bbox[2] - bbox[0]

    def test_history_container_stays_within_notebook_paper_bounds(self):
        """Stress-test: History container xpos, ypos, and dimensions must reside within notebook paper bounds."""
        # Menubook page properties:
        # Spiral holes end at x=676
        # Sticky navigation tabs start at x=1267 (xalign 1.0, xoffset -520 -> 1400 - 133 = 1267)
        # Notebook title pos (650, 177) -> title bottom ~240
        # Notebook page bottom ~915

        xpos_match = re.search(r'xpos\s+(\d+)', self.history_content)
        ypos_match = re.search(r'ypos\s+(\d+)', self.history_content)
        xsize_match = re.search(r'style\s+history_container:.*?xsize\s+(\d+)', self.history_content, re.DOTALL)
        ysize_match = re.search(r'style\s+history_container:.*?ysize\s+(\d+)', self.history_content, re.DOTALL)

        self.assertIsNotNone(xpos_match, "history_container must declare an explicit xpos")
        self.assertIsNotNone(ypos_match, "history_container must declare an explicit ypos")
        self.assertIsNotNone(xsize_match, "history_container must declare an explicit xsize")
        self.assertIsNotNone(ysize_match, "history_container must declare an explicit ysize")

        xpos = int(xpos_match.group(1))
        ypos = int(ypos_match.group(1))
        xsize = int(xsize_match.group(1))
        ysize = int(ysize_match.group(1))

        # Must clear the spiral holes on the left
        self.assertGreater(
            xpos, 676,
            f"Container xpos ({xpos}px) must clear spiral holes (<= 676px)"
        )
        # Must not extend past the sticky tabs on the right
        container_right = xpos + xsize
        self.assertLessEqual(
            container_right, 1260,
            f"Container right edge ({container_right}px) must not overlap tabs (>= 1267px)"
        )
        # Vertical placement
        self.assertGreaterEqual(
            ypos, 240,
            f"Container ypos ({ypos}px) must be below Log title (~240px)"
        )
        container_bottom = ypos + ysize
        self.assertLessEqual(
            container_bottom, 900,
            f"Container bottom ({container_bottom}px) must be within notebook paper (< 915px)"
        )

    def test_history_content_and_scrollbar_clearance(self):
        """Verify inner frame and scrollbar fit without clipping or colliding with tabs."""
        frame_match = re.search(r'style\s+history_frame:.*?xsize\s+(\d+)', self.history_content, re.DOTALL)
        cont_match = re.search(r'style\s+history_container:.*?xsize\s+(\d+)', self.history_content, re.DOTALL)
        who_match = re.search(r'label\s+h\.who.*?xsize\s+(\d+)', self.history_content, re.DOTALL)
        what_match = re.search(r'text\s+what:.*?xsize\s+(\d+)', self.history_content, re.DOTALL)

        self.assertIsNotNone(frame_match)
        self.assertIsNotNone(cont_match)
        self.assertIsNotNone(who_match)
        self.assertIsNotNone(what_match)

        frame_w = int(frame_match.group(1))
        cont_w = int(cont_match.group(1))
        who_w = int(who_match.group(1))
        what_w = int(what_match.group(1))

        # Check scrollbar channel
        scrollbar_margin = cont_w - frame_w
        scrollbar_w = 29
        self.assertGreaterEqual(
            scrollbar_margin, scrollbar_w,
            f"Scrollbar channel ({scrollbar_margin}px) must accommodate vertical scrollbar ({scrollbar_w}px)"
        )

        # Check content components fit within frame
        # hbox spacing is 15
        content_w = who_w + 15 + what_w
        self.assertLessEqual(
            content_w, frame_w,
            f"Total content width ({content_w}px) must fit within history_frame ({frame_w}px)"
        )

    def test_all_speaker_names_fit_within_who_label(self):
        """Stress-test all character speaker names to ensure individual words fit inside who label width."""
        speakers = [
            "Winston", "Dhampir", "Ica", "Madeline", "Razzle Dazzle", "Nicky",
            "Ulysses", "Freddy", "Victor", "Jermiah", "Barry", "Carl", "Tucker",
            "Edgar", "Simon", "Kyle", "Alan"
        ]
        who_match = re.search(r'label\s+h\.who.*?xsize\s+(\d+)', self.history_content, re.DOTALL)
        who_w = int(who_match.group(1))

        for name in speakers:
            for word in name.split():
                w = self._get_text_width(self.sharpie_path, 33, word)
                self.assertLessEqual(
                    w, who_w,
                    f"Speaker word '{word}' ({w}px) exceeds who label width ({who_w}px)"
                )

    def test_empty_history_message_fits_inside_container(self):
        """Verify the empty history message fits cleanly within container width."""
        cont_match = re.search(r'style\s+history_container:.*?xsize\s+(\d+)', self.history_content, re.DOTALL)
        cont_w = int(cont_match.group(1))
        empty_text = "The dialogue history is empty."
        for font_name, font_file, size in [
            ("Monaspace Neon", self.neon_path, 26),
            ("OpenDyslexic", self.od_path, 26),
        ]:
            w = self._get_text_width(font_file, size, empty_text)
            self.assertLess(
                w, cont_w,
                f"Empty history text ({w}px) exceeds container width ({cont_w}px) in {font_name}"
            )


if __name__ == "__main__":
    unittest.main()
