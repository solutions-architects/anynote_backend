from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse

from rest_framework import generics, permissions, response, status
from rest_framework.generics import GenericAPIView

import jwt
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import EmailVerificationSerializer, RegisterSerializer, EmailTokenObtainSerializer
from .utils import EmailSender


class RegisterView(generics.CreateAPIView):
    """
    API view for registration

    Send email with a confirmation link
    to the user`s mailbox after registration
    """

    queryset = get_user_model().objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer

    @swagger_auto_schema(request_body=RegisterSerializer)
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
    
        user_data = serializer.data

        user = get_user_model().objects.get(email=user_data['email'])
        tokens = RefreshToken.for_user(user).access_token

        # Create the link that will redirect the user to the verification page
        current_site = get_current_site(request).domain
        relative_link = reverse('email-verify')

        absurl = f'http://{current_site}{relative_link}?token={tokens}' 
        'http://' + 'localhost:5173/verify-email' + '?token=' + str(tokens)

        email_body = 'Welcome to the club, buddy\n'\
        + 'Click the link below to verify your email\n{absurl}'

        email_data = {
            'email_body': email_body, 
            'to_email': user.email,
            'email_subject': 'Verify your email'
        }

        EmailSender.send_email(data=email_data)

        return response.Response({'access' : str(tokens), 'address:':absurl}, status=status.HTTP_201_CREATED)

regView = RegisterView.as_view()

class VerifyEmail(GenericAPIView):
    """
    Functionality of the verification page

    Get the token (token_param_config) of user and
    make the matched user verified if it is not verified
    """

    serializer_class = EmailVerificationSerializer

    #Description of the parameter for swagger
    token_param_config = openapi.Parameter(
        'token', 
        in_=openapi.IN_QUERY, 
        description='Description', 
        type=openapi.TYPE_STRING
    )

    @swagger_auto_schema(manual_parameters=[token_param_config])
    def get(self, request):
        token = request.GET.get('token')
        try:
            payload = jwt.decode(token, options={"verify_signature": False})
            user = get_user_model().objects.get(id=payload['user_id'])
            if not user.is_verified:
                user.is_verified = True
                user.save()
            return response.Response({'email': 'Successfully activated'}, status=status.HTTP_200_OK)
        except jwt.ExpiredSignatureError:
            return response.Response({'error': 'Activation expired'}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError:
            return response.Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)

verEmail = VerifyEmail.as_view()

class EmailTokenObtainPairView(TokenObtainPairView):
    serializer_class = EmailTokenObtainSerializer

emailTokenObtainPairView = EmailTokenObtainPairView.as_view()
