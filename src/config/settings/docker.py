# IN_DOCKER gets imported from settings.__init__.py by split_settings
# MIDDLEWARE gets imported from settings.__init__.py by split_settings
if IN_DOCKER:  # type: ignore # noqa: F821
    assert MIDDLEWARE[:1] == [  # type: ignore # noqa: F821
        "django.middleware.security.SecurityMiddleware"
    ]
