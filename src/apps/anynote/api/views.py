"""Anynote API views."""

from rest_framework import generics

from src.apps.anynote.models import Folder, Note

from .serializers import FolderSerializer, NoteSerializer

# Notes endpoints

class NoteAPIListCreate(generics.ListCreateAPIView):
    """Note API list and create view."""
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def get_queryset(self):
        """Return queryset of user's notes."""
        return Note.objects.filter(user=self.request.user)


class NoteAPIRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """Note API update view."""
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def get_queryset(self):
        """Return queryset of user's notes."""
        return Note.objects.filter(user=self.request.user)


noteApiListCreate = NoteAPIListCreate.as_view()

noteApiRetrieveUpdateDestroy = NoteAPIRetrieveUpdateDestroy.as_view()

# Folders endpoints

class FolderAPIListCreate(generics.ListCreateAPIView):
    """Folder API views set."""
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer

    # TODO! RESTRICT THE QUERYSET WHEN AUTHENTICATION IS READY
    # def get_queryset(self):
    #     """Return queryset of user's folders."""
    #     return Folder.objects.filter(user=self.request.user)


class FolderAPIRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """Folder API views set."""
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer

    # TODO! RESTRICT THE QUERYSET WHEN AUTHENTICATION IS READY
    # def get_queryset(self):
    #     """Return queryset of user's folders."""
    #     return Folder.objects.filter(user=self.request.user)


folderApiListCreate = FolderAPIListCreate.as_view()

folderApiRetrieveUpdateDestroy = FolderAPIRetrieveUpdateDestroy.as_view()
