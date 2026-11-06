from .base import *

DEBUG = True
SECRET_KEY = env("SECRET_KEY", default="dev-only-change-before-production-please")
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=["localhost", "127.0.0.1"])
EMAIL_BACKEND = env("EMAIL_BACKEND", default="django.core.mail.backends.console.EmailBackend")
