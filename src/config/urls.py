from django.contrib import admin
from django.urls import include, path

from src.apps.anynote.urls import urlpatterns as anynote_urlpatterns

api_urlpatterns = []
"""Aggregate all urls from apps APIs."""
api_urlpatterns += anynote_urlpatterns


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(api_urlpatterns)),
    # all given API routes will start with api/...
]
