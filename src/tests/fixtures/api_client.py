from rest_framework.test import APIClient

import pytest


@pytest.fixture()
def unauthenticated_client() -> APIClient:
    """
    Fixture to provide an API client

    :return: APIClient
    """
    yield APIClient()


@pytest.fixture()
def authenticated_client(unauthenticated_client) -> APIClient:
    data = {
        "username": "testUser",
        "email": "testemail@mail.com",
        "password": "TestPass1",
        "password2": "TestPass1",
    }

    response = unauthenticated_client.post("/api/auth/reg/", data=data, format="json")
    assert response.status_code == 201

    data = {
        "username": data["username"],
        "password": data["password"],
    }

    response = unauthenticated_client.post("/api/token/", data=data, format="json")
    assert response.status_code == 200
    assert "access" in response.data

    token = response.data["access"]
    unauthenticated_client.credentials(HTTP_AUTHORIZATION="Bearer " + token)
    return unauthenticated_client
