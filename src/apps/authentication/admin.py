# Register your models here.

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


class CustomUserModel(UserAdmin):
    list_display = ("id", "username", "email", "first_name",
                    "last_name", "is_verified")

admin.site.register(User, CustomUserModel)
