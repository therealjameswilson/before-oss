import tempfile
import unittest
from pathlib import Path

from scripts.hash_tree import tree_digest


class HashTreeTests(unittest.TestCase):
    def test_tree_digest_is_creation_order_independent(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            first = root / "first"
            second = root / "second"
            first.mkdir()
            second.mkdir()
            (first / "z.txt").write_bytes(b"last")
            (first / "a.txt").write_bytes(b"first")
            (second / "a.txt").write_bytes(b"first")
            (second / "z.txt").write_bytes(b"last")

            first_result = tree_digest(first)
            second_result = tree_digest(second)

            self.assertEqual(first_result["files"], 2)
            self.assertEqual(second_result["files"], 2)
            self.assertEqual(first_result["bytes"], 9)
            self.assertEqual(second_result["bytes"], 9)
            self.assertEqual(first_result["sha256"], second_result["sha256"])

    def test_tree_digest_changes_when_content_changes_at_same_path(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "record.json").write_bytes(b'{"status":"one"}')
            before = tree_digest(root)["sha256"]
            (root / "record.json").write_bytes(b'{"status":"two"}')
            after = tree_digest(root)["sha256"]

            self.assertNotEqual(before, after)

    def test_tree_digest_rejects_symlinks(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            target = root / "target.txt"
            target.write_text("source", encoding="utf-8")
            (root / "alias.txt").symlink_to(target)

            with self.assertRaisesRegex(ValueError, "symbolic link"):
                tree_digest(root)


if __name__ == "__main__":
    unittest.main()
