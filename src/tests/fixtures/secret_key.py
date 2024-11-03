from django.test import override_settings

import pytest


@pytest.fixture(autouse=True)
def test_settings(settings):
    """
    Override Django SECRET_KEY setting.

    This fixture sets django secret key.
    The secret key `IS NOT` set in ``settings.testing.py`` to make sure
    that in testing a developer `does actually use` ``settings.testing.py`` and not the other.

    ``with`` context manager is a special syntax for pytest autousable fixtures.
    """
    settings.SIMPLE_JWT["SIGNING_KEY"] = "test_secretkey"  # Must be set in order to allow SIMPLE_JWT to sign tokens
    # If it will be not set, then the notImplemented SIGN_KEY error will be thrown
    # It behaves like this because the SIMPLE_JWT sets the SIGN_KEY == SECRET_KEY and the SECRET_KEY (in local test settings) is not set by default
    # and this fixture sets it (obviously after the SIGN_KEY == SECRET_KEY happens in rest_framework.py).
    with override_settings(
        SECRET_KEY="test_secretkey",
    ):
        yield
