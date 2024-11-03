import logging

from rich.logging import RichHandler

FORMAT = "%(asctime)s %(levelname)s %(name)s %(message)s"
logging.basicConfig(
    level="NOTSET",
    format=FORMAT,
    handlers=[
        RichHandler(),
    ],
)
log = logging.getLogger("test_log")


def test_user_registration(api_client, db, settings) -> None:
    """Test the user registration API."""

    log.info(f"SECRET_KEY:{settings.SECRET_KEY}")

    data = {
        "username": "testUser",
        "email": "testemail@mail.com",
        "password": "TestPass1",
        "password2": "TestPass1",
    }

    response = api_client.post("/api/auth/reg/", data=data, format="json")
    user_id = response.data["id"]
    log.info(f"Registered user with id: {user_id}")
    log.info(f"Response: {response.data}")
    assert response.status_code == 201
    assert response.data["username"] == data["username"]
    assert response.data["email"] == data["email"]

    data = {
        "username": data["username"],
        "password": data["password"],
    }

    log.info(f"data: {data}")

    response = api_client.post("/api/token/", data=data, format="json")
    assert response.status_code == 200
