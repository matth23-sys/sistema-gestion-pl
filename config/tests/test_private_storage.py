from pathlib import Path
from django.conf import settings
from django.test import SimpleTestCase
from django.urls import resolve, Resolver404


class PrivateStorageBaselineTests(SimpleTestCase):
    def test_private_documents_are_outside_public_storage(self):
        private = Path(settings.PRIVATE_STORAGE_ROOT).resolve()
        for public in (settings.STATIC_ROOT, settings.MEDIA_ROOT):
            self.assertFalse(private.is_relative_to(Path(public).resolve()))
            self.assertFalse(Path(public).resolve().is_relative_to(private))

    def test_private_files_do_not_have_a_public_url_route(self):
        with self.assertRaises(Resolver404):
            resolve("/storage/private/contracts/example.pdf")

    def test_private_document_paths_are_distinct(self):
        paths = (
            settings.PRIVATE_CONTRACTS_ROOT,
            settings.PRIVATE_ESTIMATES_ROOT,
            settings.PRIVATE_INVOICES_ROOT,
            settings.PRIVATE_SIGNATURES_ROOT,
            settings.PRIVATE_PROJECT_PHOTOS_ROOT,
        )
        self.assertEqual(len({Path(p).resolve() for p in paths}), len(paths))
        self.assertTrue(all(Path(p).resolve().is_relative_to(Path(settings.PRIVATE_STORAGE_ROOT).resolve()) for p in paths))
