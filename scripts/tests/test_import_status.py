"""Focused integrity tests for scripts/import_status.py."""

import importlib.util
import io
import json
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "import_status.py"
SPEC = importlib.util.spec_from_file_location("import_status", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
import_status = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(import_status)


EXPECTED = "a" * 64


class ValidateConceptDigestsTest(unittest.TestCase):
    def test_accepts_matching_digest(self) -> None:
        errors = import_status.validate_concept_digests(
            "/sources/cleared.md",
            {"sha256": EXPECTED},
            [{"concept": "world/cleared.md", "sha256": EXPECTED}],
        )

        self.assertEqual(errors, [])

    def test_rejects_missing_digest(self) -> None:
        errors = import_status.validate_concept_digests(
            "/sources/private.md",
            {"sha256": EXPECTED},
            [{"concept": "world/private.md", "sha256": None}],
        )

        self.assertEqual(len(errors), 1)
        self.assertIn("missing a valid sha256", errors[0])
        self.assertIn(EXPECTED, errors[0])

    def test_rejects_mismatched_digest(self) -> None:
        actual = "b" * 64
        errors = import_status.validate_concept_digests(
            "/sources/private.md",
            {"sha256": EXPECTED},
            [{"concept": "world/private.md", "sha256": actual}],
        )

        self.assertEqual(len(errors), 1)
        self.assertIn(actual, errors[0])
        self.assertIn(EXPECTED, errors[0])


class ReferencedResourcesTest(unittest.TestCase):
    def test_carries_the_concept_digest(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            codex = Path(temp_dir)
            (codex / "world").mkdir()
            (codex / "world" / "sample.md").write_text(
                "---\n"
                "sources:\n"
                "  - resource: /sources/cleared.md\n"
                f"    sha256: {EXPECTED}\n"
                "---\n",
                encoding="utf-8",
            )
            original_codex = import_status.CODEX
            try:
                import_status.CODEX = codex
                refs = import_status.referenced_resources()
            finally:
                import_status.CODEX = original_codex

        self.assertEqual(refs["cleared.md"][0]["sha256"], EXPECTED)


class ImportStatusIntegrityTest(unittest.TestCase):
    def test_mismatched_local_only_citation_is_an_integrity_error(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            sources = root / "sources"
            codex = root / "codex"
            manifest = root / "docs" / "source-ingestion-manifest.md"
            sources.mkdir()
            (codex / "world").mkdir(parents=True)
            (codex / "world" / "private.md").write_text(
                "---\n"
                "sources:\n"
                "  - resource: /sources/private.md\n"
                f"    sha256: {'b' * 64}\n"
                "---\n",
                encoding="utf-8",
            )
            manifest.parent.mkdir()
            manifest.write_text(
                "---\n"
                "sources:\n"
                "  - resource: /sources/private.md\n"
                f"    sha256: {EXPECTED}\n"
                "    disposition: partial\n"
                "    availability: local-only\n"
                "---\n",
                encoding="utf-8",
            )
            original_paths = (import_status.SOURCES, import_status.CODEX, import_status.MANIFEST)
            original_argv = sys.argv
            output = io.StringIO()
            try:
                import_status.SOURCES = sources
                import_status.CODEX = codex
                import_status.MANIFEST = manifest
                sys.argv = ["import_status.py", "--json"]
                with redirect_stdout(output):
                    result = import_status.main()
            finally:
                import_status.SOURCES, import_status.CODEX, import_status.MANIFEST = original_paths
                sys.argv = original_argv

        report = json.loads(output.getvalue())
        self.assertEqual(result, 2)
        self.assertEqual(len(report["unavailable_local"]), 1)
        self.assertIn("has sha256", report["manifest_errors"][0])


if __name__ == "__main__":
    unittest.main()
