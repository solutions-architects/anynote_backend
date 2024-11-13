"""Anynote API views."""

from rest_framework import generics, permissions

from rest_framework_simplejwt.authentication import JWTAuthentication

from src.apps.anynote.models import Folder, Note

from .serializers import FolderSerializer, NoteSerializer

# Notes endpoints

class NoteAPIListCreate(generics.ListCreateAPIView):
    """Note API list and create view."""
    serializer_class = NoteSerializer

    authentication_classes = [JWTAuthentication]
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        """Return queryset of user's notes."""
        return Note.objects.filter(user=self.request.user)


class NoteAPIRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """Note API update view."""
    serializer_class = NoteSerializer

    authentication_classes = [JWTAuthentication]
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        """Return queryset of user's notes."""
        return Note.objects.filter(user=self.request.user)


noteApiListCreate = NoteAPIListCreate.as_view()

noteApiRetrieveUpdateDestroy = NoteAPIRetrieveUpdateDestroy.as_view()

# Folders endpoints

class FolderAPIListCreate(generics.ListCreateAPIView):
    """Folder API views set."""
    serializer_class = FolderSerializer

    authentication_classes = [JWTAuthentication]
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
         """Return queryset of user's folders."""
         return Folder.objects.filter(user=self.request.user)


class FolderAPIRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """Folder API views set."""
    serializer_class = FolderSerializer

    authentication_classes = [JWTAuthentication]
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        """Return queryset of user's folders."""
        return Folder.objects.filter(user=self.request.user)


folderApiListCreate = FolderAPIListCreate.as_view()

folderApiRetrieveUpdateDestroy = FolderAPIRetrieveUpdateDestroy.as_view()

class FolderAPIChildNotesList(generics.ListAPIView):
    "List/Create views set for a folders child notes."
    serializer_class = NoteSerializer

    authentication_classes = [JWTAuthentication]
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        pk = self.kwargs["pk"] # primary key of a folder
        folder = Folder.objects.get(id=pk)
        return folder.notes.all()

class FolderAPIChildFoldersList(generics.ListAPIView):
    "List/Create views set for a folders child folders."
    serializer_class = FolderSerializer

    authentication_classes = [JWTAuthentication]
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        pk = self.kwargs["pk"] # primary key of a folder
        folder = Folder.objects.get(id=pk)
        return folder.folders.all()

folderApiChildNotesList = FolderAPIChildNotesList.as_view()

folderApiChildFoldersList = FolderAPIChildFoldersList.as_view()
