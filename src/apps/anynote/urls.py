"""Anynote app urls."""

from django.urls import path

from .api.views import (
    folderApiChildFoldersList,
    folderApiChildNotesList,
    folderApiListCreate,
    folderApiRetrieveUpdateDestroy,
    noteApiListCreate,
    noteApiRetrieveUpdateDestroy,
)

urlpatterns = [
    path("notes/", noteApiListCreate),
    path("notes/<int:pk>", noteApiRetrieveUpdateDestroy, name="notes-detail"),
    path("folders/", folderApiListCreate),
    path("folders/<int:pk>", folderApiRetrieveUpdateDestroy, name="folders-detail"),
    path("folders/<int:pk>/notes", folderApiChildNotesList),
    path("folders/<int:pk>/folders", folderApiChildFoldersList),
]
