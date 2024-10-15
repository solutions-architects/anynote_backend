"""Anynote app urls."""

from django.urls import path

from .api.views import (
    folderApiListCreate,
    folderApiRetrieveUpdateDestroy,
    noteApiListCreate,
    noteApiRetrieveUpdateDestroy,
)

urlpatterns = [
    path(
        "note/",
        noteApiListCreate,
    ),
    path(
        "note/<int:pk>",
        noteApiRetrieveUpdateDestroy,
    ),
    path(
        "folder/",
        folderApiListCreate,
    ),
    path(
        "folder/<int:pk>",
        folderApiRetrieveUpdateDestroy,
    ),
]
