from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from oss_research import provenance


class ProvenanceTests(unittest.TestCase):
    def test_rebuild_preserves_dates_for_same_frozen_source(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            project_root = Path(directory)
            pdf_path = (
                project_root / "data" / "source" / "personnel-database.pdf"
            )
            pdf_path.parent.mkdir(parents=True)
            pdf_path.write_bytes(b"stable test PDF")
            provenance_dir = project_root / "data" / "provenance"

            with (
                mock.patch.object(provenance, "PROJECT_ROOT", project_root),
                mock.patch.object(
                    provenance, "PROVENANCE_DIR", provenance_dir
                ),
                mock.patch.object(
                    provenance, "pdf_page_count", return_value=1
                ),
            ):
                provenance.build_source_manifest(
                    pdf_path,
                    retrieval_method="test fixture",
                    original_input_path="personnel-database.pdf",
                    official_copy_verified=True,
                )
                output = provenance_dir / "source_manifest.json"
                existing = json.loads(output.read_text(encoding="utf-8"))
                existing["created_at"] = "2001-02-03"
                existing["sources"][0]["retrieval_date"] = "2001-02-03"
                for item in existing["official_documentation_accessed"]:
                    item["access_date"] = "2001-02-04"
                existing.pop("manifest_sha256_before_checksum_field", None)
                existing_bytes = (
                    json.dumps(existing, indent=2, ensure_ascii=False) + "\n"
                ).encode("utf-8")
                existing["manifest_sha256_before_checksum_field"] = (
                    hashlib.sha256(existing_bytes).hexdigest()
                )
                output.write_text(
                    json.dumps(existing, indent=2, ensure_ascii=False) + "\n",
                    encoding="utf-8",
                )

                rebuilt = provenance.build_source_manifest(
                    pdf_path,
                    retrieval_method="test fixture",
                    original_input_path="personnel-database.pdf",
                    official_copy_verified=True,
                )

        self.assertEqual(rebuilt["created_at"], "2001-02-03")
        self.assertEqual(
            rebuilt["sources"][0]["retrieval_date"], "2001-02-03"
        )
        self.assertEqual(
            {
                item["access_date"]
                for item in rebuilt["official_documentation_accessed"]
            },
            {"2001-02-04"},
        )


if __name__ == "__main__":
    unittest.main()
