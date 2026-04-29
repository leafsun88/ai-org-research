import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path


MODULE_DIR = Path(__file__).resolve().parent
MODULE_PATH = MODULE_DIR / "migrate_project_structure.py"


def load_module():
    spec = importlib.util.spec_from_file_location("migrate_project_structure", MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    sys.modules["migrate_project_structure"] = module
    spec.loader.exec_module(module)
    return module


class ProjectStructureMigrationTests(unittest.TestCase):
    def test_youtube_root_file_classification(self):
        migration = load_module()
        root = Path("/repo/companies/lovable/vault/youtube")

        self.assertEqual(
            migration.classify_vault_child("youtube", root / "2026-04-20_interview.md", root),
            root / "transcripts" / "2026-04-20_interview.md",
        )
        self.assertEqual(
            migration.classify_vault_child("youtube", root / "_youtube_candidates.json", root),
            root / "metadata" / "_youtube_candidates.json",
        )
        self.assertEqual(
            migration.classify_vault_child("youtube", root / "2026-04-20_interview.segments.json", root),
            root / "metadata" / "2026-04-20_interview.segments.json",
        )

    def test_substack_and_podcast_essence_renames(self):
        migration = load_module()
        substack = Path("/repo/companies/lovable/vault/substack")
        podcasts = Path("/repo/companies/lovable/vault/podcasts")

        self.assertEqual(
            migration.classify_vault_child("substack", substack / "source-essence" / "note.md", substack),
            substack / "essence" / "note.md",
        )
        self.assertEqual(
            migration.classify_vault_child("podcasts", podcasts / "podcast-essence" / "ep.md", podcasts),
            podcasts / "essence" / "ep.md",
        )
        self.assertEqual(
            migration.classify_vault_child("podcasts", podcasts / "_podcast_query_map.md", podcasts),
            podcasts / "metadata" / "_podcast_query_map.md",
        )

    def test_unique_destination_preserves_collisions(self):
        migration = load_module()
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp) / "target.md"
            base.write_text("existing", encoding="utf-8")
            self.assertEqual(migration.unique_destination(base), Path(tmp) / "target_2.md")


if __name__ == "__main__":
    unittest.main()
