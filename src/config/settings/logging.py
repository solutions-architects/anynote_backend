import logging
import logging.config
import os

# use this - logging.basicConfig(level=logging.DEBUG), while writing your own logs to catch all the levels


class InfoFilter(logging.Filter):
    def filter(self, record):
        return record.levelno == logging.INFO


logs_folder = "logs"
log_file = os.path.join(logs_folder, "debug.log")

if not os.path.exists(logs_folder):
    os.makedirs(logs_folder)

if not os.path.exists(log_file):
    open(log_file, "a").close()

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {"standard": {"format": "%(asctime)s %(levelname)s %(name)s %(message)s"}},
    "handlers": {
        "console": {"level": "INFO", "class": "rich.logging.RichHandler", "formatter": "standard", "filters": []},
        "file": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "filename": "logs/debug.log",
            "encoding": "utf-8",
            "formatter": "standard",
            "filters": ["info_filter"],
        },
    },
    "loggers": {
        logger_name: {
            "level": "INFO",
            "propagate": True,
        }
        for logger_name in ("django", "django.request", "django.db.backends", "django.template", "src", "console")
    },
    "filters": {"info_filter": {"()": "src.config.settings.InfoFilter"}},
    "root": {
        "handlers": ["console", "file"],
        "level": "INFO",
    },
}
