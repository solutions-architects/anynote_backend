from django.contrib import admin
from django.urls import include, path

from src.apps.anynote.urls import urlpatterns as anynote_urlpatterns
from src.apps.authentication.urls import urlpatterns as authentication_urlpatterns

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Products API",
      default_version='v1',
      description="Description Puk-Puk",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="Goida@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

api_urlpatterns = []
"""Aggregate all urls from apps APIs."""
api_urlpatterns += anynote_urlpatterns
api_urlpatterns += authentication_urlpatterns


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(api_urlpatterns)),
    # all given API routes will start with api/...
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('json/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
]
