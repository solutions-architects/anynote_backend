"""Settings file that is used when running app in github action."""

DEBUG = True
SECRET_KEY = "githubworkflowdjangosecretkey"


# Use production database settings for github actions environment
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "postgres",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "db",
        "PORT": "5432",
        "ATOMIC_REQUESTS": True,
        "CONN_MAX_AGE": 600,
    }
}
