from django.test import override_settings

import pytest


@pytest.fixture(autouse=True)
def test_settings(settings):
    """
    Override Django SECRET_KEY setting.

    This fixture sets django secret key.
    The secret key `IS NOT` set in ``settings.unittest.py`` to make sure
    that in testing a developer `does actually use` ``settings.unittest.py`` and not the other.

    ``with`` context manager is a special syntax for pytest autousable fixtures.
    """
    with override_settings(
        SECRET_KEY="pytestdjangosecretkey",
    ):
        yield
