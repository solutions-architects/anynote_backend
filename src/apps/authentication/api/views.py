from django.contrib.auth.models import User
from rest_framework import generics, permissions
from .serializers import RegisterSerializer
class RegisterView(generics.CreateAPIView):

    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer

regView = RegisterView.as_view()






