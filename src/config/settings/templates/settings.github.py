"""Settings file that is used when running app in github action."""

DEBUG = True
SECRET_KEY = "githubworkflowdjangosecretkey"


# Due to unexpected errors with db connection in pytest-django (some `Temporary failure in name resolution` that is unrepeatable in non github actions environment)
# SQLite is used as the database in github actions
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",  # type: ignore  # noqa: F821
        # SQLite database for tests in github actions
    }
}
