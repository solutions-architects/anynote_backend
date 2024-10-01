import os.path
from pathlib import Path

from split_settings.tools import include, optional

from src.general.tests.pytest import is_testing

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

# Prefix for project environment variables namespace.
# IMPORTANT! If you want to change this const you must also change all env vars that start with this prefix.
ENVIRONMENT_PREFIX = "DJANGO_PROJECT_"

LOCAL_SETTINGS_PATH: str | None = os.getenv(f"{ENVIRONMENT_PREFIX}LOCAL_SETTINGS_PATH")

if not LOCAL_SETTINGS_PATH:
    LOCAL_SETTINGS_PATH = "local/settings.dev.py"

    if is_testing():
        LOCAL_SETTINGS_PATH = "local/settings.testing.py"

if not os.path.isabs(LOCAL_SETTINGS_PATH):
    LOCAL_SETTINGS_PATH = str(BASE_DIR / LOCAL_SETTINGS_PATH)

# Order of the settings loading
include(
    "logging.py",
    "base.py",
    "app_specific.py",
    optional(LOCAL_SETTINGS_PATH),
    "environment.py",
    "docker.py",
)

# SECRET_KEY assertion guarantees that a developer will not accidentally use prod or dev settings for testing
# The SECRET_KEY for testing will be set later as a pytest autouse fixture in general/tests/fixtures/secret_key.
if not is_testing():
    assert SECRET_KEY is not NotImplemented  # type: ignore # noqa: F821
    # Check if database settings are not set by default
    assert DATABASES.get("default") is not None  # type: ignore # noqa: F821
