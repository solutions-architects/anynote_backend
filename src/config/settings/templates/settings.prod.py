"""Template for production settings."""

DEBUG = False
# Generate new secret key with the production_data.py script
SECRET_KEY = "secret_key"

EMAIL_HOST_PASSWORD = 'mcqb jsgo zvki aznt'

IN_DOCKER = True

# Database settings must be same in docker-compose.yml
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
