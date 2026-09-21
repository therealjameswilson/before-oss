"""The LoC context review aid must stay bounded and read-only."""

from __future__ import annotations

import unittest

from scripts.inspect_loc_candidates import (
    BATCH_NAME_RE,
    bounded_ocr_context,
    full_text,
    full_text_service_url,
    item_json_url,
    relevant_snippet,
    text_service_url,
)


class LocContextReviewTests(unittest.TestCase):
    def test_current_and_legacy_batch_names_are_safe(self) -> None:
        for name in (
            "batch-619",
            "page-271-lee-lefferts-b620",
            "page-274-lester-letellier-b620",
        ):
            with self.subTest(name=name):
                self.assertIsNotNone(BATCH_NAME_RE.fullmatch(name))
        for name in ("../batch-619", "Batch-619", "batch 619", "batch_619", ""):
            with self.subTest(name=name):
                self.assertIsNone(BATCH_NAME_RE.fullmatch(name))

    def test_item_url_uses_official_host_and_single_page(self) -> None:
        self.assertEqual(
            item_json_url("https://www.loc.gov/resource/sn83045462/1948-10-18/ed-1/?sp=20"),
            "https://www.loc.gov/resource/sn83045462/1948-10-18/ed-1/?fo=json&sp=20",
        )

    def test_rejects_foreign_hosts_and_unbounded_pages(self) -> None:
        for url in (
            "https://loc.gov.evil.example/resource/x?sp=1",
            "https://www.loc.gov/resource/x?sp=0",
            "https://www.loc.gov/resource/x?sp=1001",
            "https://www.loc.gov/resource/x?sp=2&sp=3",
            "https://www.loc.gov/resource/x",
        ):
            with self.subTest(url=url), self.assertRaises(ValueError):
                item_json_url(url)

    def test_text_service_query_is_encoded_and_segment_constrained(self) -> None:
        url = text_service_url("/service/ndnp/foo.xml", "Di Domenico")
        self.assertIn("https://tile.loc.gov/text-services/word-coordinates-service?", url)
        self.assertIn("q=Di+Domenico", url)
        self.assertIn("relevant_snippet=1", url)
        with self.assertRaises(ValueError):
            text_service_url("https://elsewhere.example/evil.xml", "Dickson")

        full_url = full_text_service_url("/service/ndnp/foo.xml")
        self.assertIn("full_text=1", full_url)
        self.assertIn("format=alto_xml", full_url)
        with self.assertRaises(ValueError):
            full_text_service_url("https://elsewhere.example/evil.xml")

    def test_snippet_removes_highlight_markers_without_mutating_source(self) -> None:
        segment = "/service/ndnp/foo.xml"
        payload = {segment: {"relevant_snippet": "[[tag]]Dickson[[/tag]] Martin"}}
        self.assertEqual(relevant_snippet(payload, segment), "Dickson Martin")
        self.assertEqual(payload[segment]["relevant_snippet"], "[[tag]]Dickson[[/tag]] Martin")
        self.assertEqual(relevant_snippet({}, segment), "")

    def test_full_text_fallback_is_bounded_and_prefers_full_name(self) -> None:
        segment = "/service/ndnp/foo.xml"
        payload = {
            segment: {
                "full_text": "Mayer generic occurrence. "
                + ("background " * 30)
                + "Lawrence J Mayer served as secretary. "
                + ("tail " * 100)
            }
        }
        source = full_text(payload, segment)
        context = bounded_ocr_context(
            source, ["Lawrence J Mayer", "Mayer"], max_chars=260
        )
        self.assertIn("Lawrence J Mayer served as secretary", context)
        self.assertNotIn("Mayer generic occurrence", context)
        self.assertLessEqual(len(context), 260)
        self.assertEqual(payload[segment]["full_text"], source)

    def test_full_text_fallback_handles_missing_terms_and_bad_bounds(self) -> None:
        self.assertEqual(bounded_ocr_context("alpha beta", ["Mayer"]), "")
        self.assertEqual(full_text({}, "/service/ndnp/foo.xml"), "")
        with self.assertRaises(ValueError):
            bounded_ocr_context("Mayer", ["Mayer"], max_chars=0)


if __name__ == "__main__":
    unittest.main()
