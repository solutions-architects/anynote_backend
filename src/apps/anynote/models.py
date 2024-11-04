import hashlib

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Note(models.Model):
    """
    Note model.

    Can be *located* inside a folder or not at any.
    """

    user = models.ForeignKey(User, related_name="notes", on_delete=models.CASCADE)
    content = models.JSONField()
    """Json field with the note structure."""

    hash = models.CharField(max_length=64)
    # SHA256 hash string is always 64 characters long

    parent = models.ForeignKey(
        "Folder", related_name="notes", related_query_name="note", blank=True, null=True, on_delete=models.CASCADE
    )
    # Folder can be inside other Folder or has no parent

    def save(self, *args, **kwags):
        self.hash = self.generate_hash()
        # The self.hash will be generated from the content of the Note.
        return super().save(*args, **kwags)

    def generate_hash(self):
        """Generate hash from Note's content."""
        str_content: str = str(self.content)
        hash_value: str = hashlib.sha256(str_content.encode("utf-8")).hexdigest()
        return hash_value  # 64 characters long string

    def get_absolute_url(self):
        """Get absolute url of a certain model instance."""
        return reverse("notes-detail", kwargs={"pk": self.pk})


class Folder(models.Model):
    """
    Folder model.

    Folder contains other folders or notes.
    """

    user = models.ForeignKey(User, related_name="folders", on_delete=models.CASCADE)

    name = models.TextField()

    parent = models.ForeignKey(
        "Folder", related_name="folders", related_query_name="folder", blank=True, null=True, on_delete=models.CASCADE
    )
    # Folder can be inside other Folder or has no parent

    def get_absolute_url(self):
        """Get absolute url of a certain model instance."""
        return reverse("folders-detail", kwargs={"pk": self.pk})
