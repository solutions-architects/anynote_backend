from django.contrib import admin

# Register your models here.
from src.apps.anynote.models import Folder, Note

admin.site.register(Note)
admin.site.register(Folder)
