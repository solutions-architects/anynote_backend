from django.contrib import admin
from django.urls import include, path

from src.api.urls import urlpatterns

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(urlpatterns)),
]
