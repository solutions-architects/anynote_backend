"""Serializers for Anynote app models."""

from rest_framework import serializers

from src.apps.anynote.models import Folder, Note


class NoteSerializer(serializers.ModelSerializer):
    """Note model serializer."""

    id = serializers.IntegerField(read_only=True)
    content = serializers.JSONField(default=dict)
    hash = serializers.CharField(read_only=True)

    class Meta:
        model = Note
        fields = "__all__"


class FolderSerializer(serializers.ModelSerializer):
    """Folder model serializer."""

    class Meta:
        model = Folder
        fields = "__all__"
