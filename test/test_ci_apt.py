"""Offline tests for the runner's APT mirror configuration."""

from pathlib import Path
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / ".github/scripts/configure-apt-mirrors.sh"


class AptMirrorTests(unittest.TestCase):
    def rewrite(self, content):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "apt-source"
            path.write_text(content, encoding="utf-8")
            subprocess.run(["bash", str(SCRIPT), str(path)], check=True)
            rewritten = path.read_text(encoding="utf-8")
            subprocess.run(["bash", str(SCRIPT), str(path)], check=True)
            self.assertEqual(rewritten, path.read_text(encoding="utf-8"))
            return rewritten

    def test_mirror_list_preserves_priorities_and_fallbacks(self):
        before = (
            "http://azure.archive.ubuntu.com/ubuntu/\tpriority:1\n"
            "https://archive.ubuntu.com/ubuntu/\tpriority:2\n"
            "https://security.ubuntu.com/ubuntu/\tpriority:3\n"
        )
        self.assertEqual(
            self.rewrite(before),
            before.replace("http://azure.archive.ubuntu.com/", "https://archive.ubuntu.com/"),
        )

    def test_deb822_preserves_signatures_and_security_suite(self):
        before = (
            "Types: deb\n"
            "URIs: https://azure.archive.ubuntu.com/ubuntu/\n"
            "Suites: noble noble-updates noble-security\n"
            "Components: main universe\n"
            "Signed-By: /usr/share/keyrings/ubuntu-archive-keyring.gpg\n"
        )
        self.assertEqual(
            self.rewrite(before),
            before.replace("https://azure.archive.ubuntu.com/", "https://archive.ubuntu.com/"),
        )

    def test_mirror_transport_and_unrelated_hosts_are_unchanged(self):
        before = (
            "URIs: mirror+file:/etc/apt/apt-mirrors.txt\n"
            "deb https://security.ubuntu.com/ubuntu/ noble-security main\n"
            "# https://azureXarchiveXubuntuXcom/ must not match escaped dots\n"
            "# https://azure.archive.ubuntu.com.example.org/ must not match\n"
        )
        self.assertEqual(self.rewrite(before), before)

    def test_missing_optional_config_is_safe(self):
        with tempfile.TemporaryDirectory() as directory:
            subprocess.run(["bash", str(SCRIPT), str(Path(directory) / "missing")], check=True)

    def test_automatic_build_workflows_use_the_fix_and_bound_installation(self):
        for name in ("deploy.yml", "unit-tests.yml", "broken-links-site.yml"):
            workflow = (ROOT / ".github/workflows" / name).read_text(encoding="utf-8")
            self.assertIn("sudo bash .github/scripts/configure-apt-mirrors.sh", workflow)
            self.assertIn("timeout-minutes: 6", workflow)
            self.assertIn("timeout 120s apt-get", workflow)
            self.assertIn("timeout 180s apt-get", workflow)


if __name__ == "__main__":
    unittest.main()
