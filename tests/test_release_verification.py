import hashlib
import importlib.util
import json
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location("verify_deployed_release", Path(__file__).resolve().parents[1] / "scripts/verify_deployed_release.py")
release = importlib.util.module_from_spec(spec)
spec.loader.exec_module(release)


class ReleaseVerificationTests(unittest.TestCase):
    def setUp(self):
        self.body = b'{"people": 3}'
        self.record = {"path": "data/stats.json", "size_bytes": len(self.body),
                       "sha256": hashlib.sha256(self.body).hexdigest()}
        self.manifest = json.dumps({"files": [self.record]}).encode()

    def fetch(self, path):
        return self.manifest if path == release.MANIFEST else self.body

    def test_exact_projection(self):
        result = release.verify_assets(self.manifest, self.fetch)
        self.assertEqual(result["assets_verified"], 1)
        self.assertEqual(result["bytes_verified"], len(self.body))

    def test_stale_manifest_is_not_success(self):
        with self.assertRaisesRegex(ValueError, "Live manifest"):
            release.verify_assets(b'{"files": []}', self.fetch)

    def test_same_size_changed_content_fails(self):
        self.body = b'{"people": 4}'
        with self.assertRaisesRegex(ValueError, "hash mismatch"):
            release.verify_assets(self.manifest, self.fetch)

    def test_truncated_content_fails(self):
        self.body = b"x"
        with self.assertRaisesRegex(ValueError, "size mismatch"):
            release.verify_assets(self.manifest, self.fetch)

    def test_unsafe_paths_rejected(self):
        for path in ("../secret", "/absolute", "//other.example/file", "data/%2e%2e/../secret", "https://other.example/file", "data/x?token=x"):
            with self.subTest(path=path), self.assertRaises(ValueError):
                release.validate_path(path)

    def test_duplicates_and_unbounded_concurrency_rejected(self):
        self.manifest = json.dumps({"files": [self.record, self.record]}).encode()
        with self.assertRaisesRegex(ValueError, "unique"):
            release.verify_assets(self.manifest, self.fetch)
        with self.assertRaisesRegex(ValueError, "concurrency"):
            release.verify_assets(self.manifest, self.fetch, workers=5)
