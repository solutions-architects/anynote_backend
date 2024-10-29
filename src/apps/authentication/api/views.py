from rest_framework import response, status
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from rest_framework import generics, permissions
from rest_framework.generics import GenericAPIView
from drf_yasg import openapi
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer, EmailVerificationSerializer
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from django.urls import reverse
import jwt


class RegisterView(generics.CreateAPIView):

    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer

    @swagger_auto_schema(request_body=RegisterSerializer)
    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user = serializer.data

        email = User.objects.get(email=user["email"])
        tokens = RefreshToken.for_user(email).access_token

        current_site = get_current_site(request).domain
        #relative_link = reverse('email-verify')
        relative_link = "dksd"
        absurl = 'http://' + current_site + relative_link + "?token=" + str(tokens)

        return response.Response({'user_data': user, 'access_token' : str(tokens), "url":absurl}, status=status.HTTP_201_CREATED)

regView = RegisterView.as_view()

class VerifyEmail(GenericAPIView):
    serializer_class = EmailVerificationSerializer

    token_param_config = openapi.Parameter(
        'token', in_=openapi.IN_QUERY, description='Description', type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[token_param_config])
    def get(self, request):
        token = request.GET.get('token')
        try:
            payload = jwt.decode(token, options={"verify_signature": False})
            print(payload)
            user = User.objects.get(id=payload['user_id'])
            if not user.is_verified:
                user.is_verified = True
                user.save()
            return response.Response({'email': 'Successfully activated'}, status=status.HTTP_200_OK)
        except jwt.ExpiredSignatureError as identifier:
            return response.Response({'error': 'Activation Expired'}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as identifier:
            return response.Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)






