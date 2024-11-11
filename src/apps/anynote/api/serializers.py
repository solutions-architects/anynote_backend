"""Serializers for Anynote app models."""

from rest_framework import serializers

from src.apps.anynote.models import Folder, Note


class NoteSerializer(serializers.ModelSerializer):
    """Note model serializer."""

    href = serializers.SerializerMethodField(method_name="get_href")

    user = serializers.PrimaryKeyRelatedField(read_only=True)

    id = serializers.IntegerField(read_only=True)
    content = serializers.JSONField(default=dict)
    hash = serializers.CharField(read_only=True)

    class Meta:
        model = Note
        fields = "__all__"  # "__all__" # ("id", "content", "hash")

    def create(self, validated_data):
        user = self.context["request"].user
        validated_data["user"] = user
        return super().create(validated_data)

    def get_href(self, obj):
        obj_url = obj.get_absolute_url()  # return the relative url
        return self.context["request"].build_absolute_uri(obj_url)  # return the absolute url of the object


class FolderSerializer(serializers.ModelSerializer):
    """Folder model serializer."""

    user = serializers.PrimaryKeyRelatedField(read_only=True)

    href = serializers.SerializerMethodField(method_name="get_href")

    class Meta:
        model = Folder
        fields = "__all__"  # "__all__" # ("id", "name")

    def create(self, validated_data):
        user = self.context["request"].user
        validated_data["user"] = user
        return super().create(validated_data)

    def get_href(self, obj):
        obj_url = obj.get_absolute_url()  # return the relative url
        return self.context["request"].build_absolute_uri(obj_url)  # return the absolute url of the object
