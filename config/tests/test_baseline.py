from unittest.mock import MagicMock, patch
from django.test import SimpleTestCase
from django.urls import reverse


class BaselineTests(SimpleTestCase):
    def test_login_route_resolves(self):
        self.assertEqual(reverse("login"), "/login/")

    def test_dashboard_requires_authentication(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 302)
        self.assertIn("/login/", response.url)

    @patch("config.views.connection")
    def test_health_check_success(self, mocked_connection):
        cursor = MagicMock()
        mocked_connection.cursor.return_value.__enter__.return_value = cursor
        response = self.client.get("/health/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["database"], "ok")

    @patch("config.views.connection")
    def test_health_check_failure(self, mocked_connection):
        mocked_connection.cursor.side_effect = RuntimeError("unavailable")
        response = self.client.get("/health/")
        self.assertEqual(response.status_code, 503)
        self.assertEqual(response.json()["database"], "error")
