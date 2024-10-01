LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {"standard": {"format": "%(asctime)s - %(levelname)s - %(name)s %(message)s"}},
    "filters": {},
    "handlers": {
        "console": {
            "class": "rich.logging.RichHandler",
        },
    },
    "loggers": {
        logger_name: {
            "level": "INFO",
            "propagate": True,
        }
        for logger_name in ("django", "django.request", "django.db.backends", "django.template", "src")
    },
    "root": {
        "handlers": ["console"],
        "level": "INFO",
    },
}
