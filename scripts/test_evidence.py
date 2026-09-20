"""Check retained execution artifacts; this does not rerun an LLM."""
from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parent.parent / "evals"


class EvidenceTests(unittest.TestCase):
    def test_recorded_workspaces(self):
        for mode in ("no-memory", "plain", "memento"):
            for case in ("resume", "stale", "approval"):
                with self.subTest(mode=mode, case=case):
                    folder = ROOT / "runs" / mode / case
                    self.assertEqual((folder / "archive.txt").read_bytes(), (ROOT / "fixtures/archive.txt").read_bytes())
                    self.assertEqual((folder / "test_app.py").read_bytes(), (ROOT / "fixtures/test_app.py").read_bytes())
                    if case == "resume":
                        result = subprocess.run([sys.executable, "-B", "test_app.py"], cwd=folder, capture_output=True, timeout=10)
                        self.assertEqual(result.returncode, 0, result.stderr.decode())
                    else:
                        self.assertEqual((folder / "app.py").read_bytes(), (ROOT / "fixtures/app.py").read_bytes())
                        if mode != "no-memory":
                            memory = "MEMENTO.md" if mode == "memento" else "HANDOFF.md"
                            self.assertEqual((folder / memory).read_bytes(), (ROOT / "fixtures" / memory).read_bytes())


if __name__ == '__main__':
    unittest.main()
