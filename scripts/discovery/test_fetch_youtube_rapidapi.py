import importlib.util
import sys
import unittest
from pathlib import Path


MODULE_DIR = Path(__file__).resolve().parent
MODULE_PATH = MODULE_DIR / "fetch_youtube.py"
sys.path.insert(0, str(MODULE_DIR))

spec = importlib.util.spec_from_file_location("fetch_youtube", MODULE_PATH)
fetch_youtube = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fetch_youtube)


class RapidAPINormalizationTests(unittest.TestCase):
    def test_normalize_metadata_search_response(self):
        payload = {
            "results": [
                {
                    "id": "abc123",
                    "videoId": "dQw4w9WgXcQ",
                    "title": "Understanding AI Concepts",
                    "channelName": "TechExplained",
                    "publishDate": "2023-10-15T14:30:00Z",
                    "matchCount": 3,
                    "aiSummary": "This video discusses AI concepts.",
                    "timestamps": [
                        {
                            "time": 120.5,
                            "formattedTime": "02:00:30",
                            "transcript": "Artificial intelligence is transforming how teams work.",
                            "context": "fuzzy",
                        }
                    ],
                }
            ]
        }

        normalized = fetch_youtube.normalize_rapidapi_search_response(
            payload,
            source_query="artificial intelligence",
        )

        self.assertEqual(len(normalized), 1)
        self.assertEqual(normalized[0]["id"], "dQw4w9WgXcQ")
        self.assertEqual(normalized[0]["video_id"], "dQw4w9WgXcQ")
        self.assertEqual(normalized[0]["channel"], "TechExplained")
        self.assertEqual(normalized[0]["date"], "2023-10-15")
        self.assertEqual(normalized[0]["match_count"], 3)
        self.assertEqual(normalized[0]["search_provider"], "rapidapi_metadata_search")
        self.assertEqual(normalized[0]["source_queries"], ["artificial intelligence"])
        self.assertEqual(normalized[0]["timestamps"][0]["formattedTime"], "02:00:30")

    def test_normalize_transcript_response(self):
        payload = {
            "success": True,
            "transcript": [
                {
                    "text": "I can almost hear the gears turning in",
                    "duration": 3.24,
                    "offset": 0.04,
                    "lang": "en",
                },
                {
                    "text": "the room today.",
                    "duration": 2.1,
                    "offset": 3.28,
                    "lang": "en",
                },
            ],
        }

        text, segments, language = fetch_youtube.normalize_rapidapi_transcript_response(payload)

        self.assertIn("gears turning", text)
        self.assertEqual(len(segments), 2)
        self.assertEqual(segments[0]["offset"], 0.04)
        self.assertEqual(language, "en")

    def test_parse_provider_order(self):
        parsed = fetch_youtube.parse_provider_order(
            "rapidapi_transcript3, youtube_transcript_api, rapidapi_transcript3, unknown",
            ["yt_dlp_subtitle"],
            {
                "rapidapi_transcript3",
                "youtube_transcript_api",
                "yt_dlp_subtitle",
            },
        )

        self.assertEqual(parsed, ["rapidapi_transcript3", "youtube_transcript_api"])

    def test_candidate_metadata_relevance_accepts_company_and_founder(self):
        candidate = {
            "title": "David Holz on Midjourney's Mission and Impact",
            "channel": "AI Research",
            "ai_summary": "An interview with the Midjourney founder.",
            "timestamps": [
                {"transcript": "David Holz explains how Midjourney thinks about community."}
            ],
            "source_queries": ["David Holz Midjourney interview"],
        }

        relevance = fetch_youtube.candidate_metadata_relevance(
            candidate,
            required_terms=["Midjourney", "David Holz"],
            query_terms=["David Holz Midjourney interview"],
            exclude_terms=[],
            min_score=3,
        )

        self.assertTrue(relevance["is_relevant"])
        self.assertIn("Midjourney", relevance["term_hits"])

    def test_candidate_metadata_relevance_rejects_unrelated_result(self):
        candidate = {
            "title": "From the Community to Our Walls Fan Art at Supercell HQ",
            "channel": "Supercell",
            "ai_summary": "A fan art showcase.",
            "timestamps": [{"transcript": "Fan art from the community."}],
            "source_queries": ["Midjourney community interview"],
        }

        relevance = fetch_youtube.candidate_metadata_relevance(
            candidate,
            required_terms=["Midjourney", "David Holz"],
            query_terms=["Midjourney community interview"],
            exclude_terms=[],
            min_score=3,
        )

        self.assertFalse(relevance["is_relevant"])
        self.assertEqual(relevance["term_hits"], [])

    def test_candidate_metadata_relevance_rejects_excluded_phrase_even_with_company_word(self):
        candidate = {
            "title": "Unveiling The Loveable Leader: Insights from Jeff G.",
            "channel": "Leadership Podcast",
            "ai_summary": "A leadership conversation.",
            "timestamps": [{"transcript": "What makes a lovable leader effective?"}],
            "source_queries": ["Lovable Anton Osika interview"],
        }

        relevance = fetch_youtube.candidate_metadata_relevance(
            candidate,
            required_terms=["Lovable", "Anton Osika"],
            query_terms=["Lovable Anton Osika interview"],
            exclude_terms=["lovable leader", "loveable leader", "Jeff G"],
            min_score=3,
        )

        self.assertFalse(relevance["is_relevant"])
        self.assertIn("exclude", relevance["reason"])

    def test_filter_low_confidence_rapidapi_candidates(self):
        candidates = [
            {
                "video_id": "-GR2rTpiqHA",
                "title": "Minecraft's Smartest Player",
                "channel": "Wemmbu",
                "match_count": 0,
                "timestamps": [],
                "ai_summary": "",
                "source_queries": ["David Holz Midjourney interview"],
            },
            {
                "video_id": "good123",
                "title": "David Holz on Midjourney",
                "channel": "Design Interview",
                "match_count": 0,
                "timestamps": [],
                "ai_summary": "",
                "source_queries": ["David Holz Midjourney interview"],
            },
            {
                "video_id": "hit123",
                "title": "Founder interview",
                "channel": "AI Podcast",
                "match_count": 2,
                "timestamps": [{"transcript": "David Holz talks about Midjourney", "context": ""}],
                "ai_summary": "",
                "source_queries": ["David Holz Midjourney interview"],
            },
        ]

        filtered, rejected = fetch_youtube.filter_low_confidence_rapidapi_candidates(candidates)

        self.assertEqual([row["video_id"] for row in filtered], ["good123", "hit123"])
        self.assertEqual(rejected[0]["video_id"], "-GR2rTpiqHA")
        self.assertEqual(rejected[0]["status"], "filtered_low_confidence_rapidapi")

    def test_dedupe_and_rank_filters_unrelated_candidates_before_download(self):
        candidates = [
            {
                "id": "bad123",
                "video_id": "bad123",
                "title": "From the Community to Our Walls Fan Art at Supercell HQ",
                "channel": "Supercell",
                "match_count": 8,
                "timestamps": [{"transcript": "Fan art from the community.", "context": ""}],
                "ai_summary": "A fan art showcase.",
                "source_queries": ["Midjourney community interview"],
                "search_providers": ["rapidapi_metadata_search"],
            },
            {
                "id": "good123",
                "video_id": "good123",
                "title": "David Holz on Midjourney's Mission and Impact",
                "channel": "AI Research",
                "match_count": 1,
                "timestamps": [
                    {"transcript": "David Holz explains how Midjourney thinks about community.", "context": ""}
                ],
                "ai_summary": "An interview with the Midjourney founder.",
                "source_queries": ["David Holz Midjourney interview"],
                "search_providers": ["rapidapi_metadata_search"],
            },
        ]

        ranked, filtered = fetch_youtube.dedupe_and_rank_candidates(
            candidates,
            focus_terms=["Midjourney", "David Holz"],
            relevance_required_terms=["Midjourney", "David Holz"],
            exclude_terms=[],
            pre_download_relevance=True,
            min_relevance_score=3,
        )

        self.assertEqual([row["video_id"] for row in ranked], ["good123"])
        self.assertEqual(filtered[0]["video_id"], "bad123")
        self.assertEqual(filtered[0]["status"], "filtered_metadata_relevance")

    def test_configured_relevance_terms_override_broad_aliases(self):
        target = {
            "company_name": "Midjourney",
            "ticker": "MIDJOURNEY",
            "aliases": ["Midjourney", "Niji", "Moodboards"],
            "founders": ["David Holz"],
            "executives": [],
        }

        terms = fetch_youtube.build_relevance_required_terms(
            target,
            "Midjourney",
            "MIDJOURNEY",
            {"relevance_terms": ["Midjourney", "David Holz", "Midjourney V8"]},
        )

        self.assertIn("Midjourney", terms)
        self.assertIn("David Holz", terms)
        self.assertNotIn("Niji", terms)
        self.assertNotIn("Moodboards", terms)


if __name__ == "__main__":
    unittest.main()
