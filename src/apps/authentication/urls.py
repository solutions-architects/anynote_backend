"""Anynote app urls."""

from django.urls import path

from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from .api.views import regView, verEmail, emailTokenObtainPairView

urlpatterns = [
    path("auth/reg/", regView, name="reg_api"),
    path("token/", emailTokenObtainPairView, name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("email-verify/", verEmail, name="email-verify"),
]
