"""Offline checks for the pinned CI image-tool installer and CLI compatibility."""

import os
from pathlib import Path
import re
import subprocess
import tempfile
import unittest
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / ".github/scripts"


class ImageToolTests(unittest.TestCase):
    def test_automatic_builds_do_not_depend_on_apt(self):
        for name in ("deploy.yml", "unit-tests.yml", "broken-links-site.yml"):
            workflow = (ROOT / ".github/workflows" / name).read_text(encoding="utf-8")
            self.assertIn("bash .github/scripts/install-imagemagick.sh", workflow)
            self.assertIn("timeout-minutes: 6", workflow)
            self.assertNotIn("apt-get", workflow)
            self.assertNotIn("sudo", workflow)

    def test_vendor_release_is_pinned_and_verified_before_execution(self):
        script = (SCRIPTS / "install-imagemagick.sh").read_text(encoding="utf-8")
        self.assertRegex(script, r'version="\d+\.\d+\.\d+-\d+"')
        self.assertRegex(script, r'sha256="[0-9a-f]{64}"')
        self.assertIn("https://github.com/ImageMagick/ImageMagick/releases/download/", script)
        self.assertLess(script.index("sha256sum --check"), script.index("--appimage-extract"))
        self.assertNotIn("curl |", script)

    def test_legacy_cli_arguments_are_preserved(self):
        with tempfile.TemporaryDirectory() as directory:
            directory = Path(directory)
            fake = directory / "AppRun"
            fake.write_text('#!/bin/sh\nprintf "%s\\n" "$@"\n', encoding="utf-8")
            fake.chmod(0o755)
            environment = dict(os.environ, IMAGEMAGICK_APP_RUN=str(fake))
            for name in ("convert", "magick", "identify", "mogrify"):
                command = directory / name
                command.write_text((SCRIPTS / "imagemagick-cli.sh").read_text(encoding="utf-8"), encoding="utf-8")
                command.chmod(0o755)
                args = ["a file.png", "-resize", "10x10"]
                output = subprocess.check_output([str(command), *args], env=environment, text=True)
                expected = args if name in ("convert", "magick") else [name, *args]
                self.assertEqual(output.splitlines(), expected)

    def test_network_coders_and_external_delegates_are_disabled(self):
        policies = ET.parse(SCRIPTS / "imagemagick-policy.xml").getroot()
        self.assertTrue(any(p.get("domain") == "delegate" and p.get("rights") == "none" for p in policies))
        denied = [p.get("pattern", "") for p in policies if p.get("domain") == "coder" and p.get("rights") == "none"]
        self.assertTrue(any("HTTPS" in pattern and "PDF" in pattern for pattern in denied))


if __name__ == "__main__":
    unittest.main()
