"""Anynote API views."""

from rest_framework import generics

from src.apps.anynote.models import Folder, Note

from .serializers import FolderSerializer, NoteSerializer

# Notes endpoints

class NoteAPIListCreate(generics.ListCreateAPIView):
    """Note API list and create view."""
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class NoteAPIRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """Note API update view."""
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


noteApiListCreate = NoteAPIListCreate.as_view()

noteApiRetrieveUpdateDestroy = NoteAPIRetrieveUpdateDestroy.as_view()

# Folders endpoints

class FolderAPIListCreate(generics.ListCreateAPIView):
    """Folder API views set."""
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer


class FolderAPIRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """Folder API views set."""
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer


folderApiListCreate = FolderAPIListCreate.as_view()

folderApiRetrieveUpdateDestroy = FolderAPIRetrieveUpdateDestroy.as_view()
