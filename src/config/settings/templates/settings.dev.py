"""Template for local development settings."""

DEBUG = True
SECRET_KEY = "some_secret_key"


# Database settings must be same in docker-compose.dev.yml
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "postgres",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "localhost",  # Localhost to use access docker container
        "PORT": "5432",  # IMPORTANT! Use different for devDatabase if tou want to use containerized postgres
        "ATOMIC_REQUESTS": True,
        "CONN_MAX_AGE": 600,
    }
}
