def test_note_creation(db, authenticated_client) -> None:
    """Test note creation."""
    data = {
        "content": {"some": "content"},
    }
    response = authenticated_client.post("/api/notes/", data=data, format="json")
    assert response.status_code == 201


def test_folder_creation(db, authenticated_client) -> None:
    """Test note creation."""
    data = {
        "name": "some_name",
    }
    response = authenticated_client.post("/api/folders/", data=data, format="json")
    assert response.status_code == 201
