from django.core.exceptions import ImproperlyConfigured
from .base import *

DEBUG = False
SECRET_KEY = env("SECRET_KEY", default="")
if len(SECRET_KEY) < 50 or SECRET_KEY in {"change-me", "unsafe-development-key"}:
    raise ImproperlyConfigured("Production requires a unique SECRET_KEY of 50+ characters")

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[])
if not ALLOWED_HOSTS or any(host in ("*", "0.0.0.0", "localhost", "127.0.0.1") for host in ALLOWED_HOSTS):
    raise ImproperlyConfigured("Set explicit public production ALLOWED_HOSTS")

if DATABASES["default"]["PASSWORD"] in ("", "change-me", "prolegacy"):
    raise ImproperlyConfigured("Set a unique POSTGRES_PASSWORD for production")

CSRF_TRUSTED_ORIGINS = env.list("CSRF_TRUSTED_ORIGINS", default=[])
if not CSRF_TRUSTED_ORIGINS or any(not item.startswith("https://") for item in CSRF_TRUSTED_ORIGINS):
    raise ImproperlyConfigured("Use explicit HTTPS CSRF_TRUSTED_ORIGINS in production")

SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = "DENY"
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = True
SECURE_SSL_REDIRECT = True
SECURE_REFERRER_POLICY = "same-origin"
SECURE_HSTS_SECONDS = env.int("SECURE_HSTS_SECONDS", default=0)
SECURE_HSTS_INCLUDE_SUBDOMAINS = env.bool("SECURE_HSTS_INCLUDE_SUBDOMAINS", default=False)
SECURE_HSTS_PRELOAD = False

# Enable only if your trusted reverse proxy OVERRIDES this header.
if env.bool("TRUST_PROXY_SSL_HEADER", default=False):
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = env("EMAIL_HOST", default="")
EMAIL_PORT = env.int("EMAIL_PORT", default=587)
EMAIL_USE_TLS = env.bool("EMAIL_USE_TLS", default=True)
EMAIL_HOST_USER = env("EMAIL_HOST_USER", default="")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD", default="")

# Do not serve uploaded files as public URLs. The default storage is private.
STORAGES["default"] = {
    "BACKEND": "django.core.files.storage.FileSystemStorage",
    "OPTIONS": {"location": str(PRIVATE_STORAGE_ROOT), "base_url": None},
}
STORAGES["private"] = STORAGES["default"].copy()
