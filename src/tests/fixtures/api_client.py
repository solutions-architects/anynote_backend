from rest_framework.test import APIClient

import pytest


@pytest.fixture()
def api_client() -> APIClient:
    """
    Fixture to provide an API client

    :return: APIClient
    """
    yield APIClient()
