"""The LoC context review aid must stay bounded and read-only."""

from __future__ import annotations

import unittest

from scripts.inspect_loc_candidates import (
    item_json_url,
    relevant_snippet,
    text_service_url,
)


class LocContextReviewTests(unittest.TestCase):
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

    def test_snippet_removes_highlight_markers_without_mutating_source(self) -> None:
        segment = "/service/ndnp/foo.xml"
        payload = {segment: {"relevant_snippet": "[[tag]]Dickson[[/tag]] Martin"}}
        self.assertEqual(relevant_snippet(payload, segment), "Dickson Martin")
        self.assertEqual(payload[segment]["relevant_snippet"], "[[tag]]Dickson[[/tag]] Martin")
        self.assertEqual(relevant_snippet({}, segment), "")


if __name__ == "__main__":
    unittest.main()
