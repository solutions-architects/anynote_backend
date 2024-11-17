from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse

from rest_framework import generics, permissions, response, status
from rest_framework.generics import GenericAPIView

import jwt
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import EmailVerificationSerializer, RegisterSerializer
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
        #create user
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user = serializer.data

        #Get user email to create new access_token for them
        email = get_user_model().objects.get(email=user["email"])
        tokens = RefreshToken.for_user(email).access_token

        #Create the link that will redirect the user to the verification page
        current_site = get_current_site(request).domain
        relative_link = reverse('email-verify')
        absurl = 'http://' + current_site + relative_link + "?token=" + str(tokens)
        email_body = ' Welcome to the club, ' + user['username'] + \
                     ' \nUse the link below to verify your email \n' + absurl

        #data for sending an email
        data = {'email_body': email_body, 'to_email': user['email'],
                'email_subject': 'Verify your email'}

        #send email
        EmailSender.send_email(data=data)

        return response.Response({'user_data': user, 'access_token' : str(tokens), "adress:":absurl}, status=status.HTTP_201_CREATED)

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
        'token', in_=openapi.IN_QUERY, description='Description', type=openapi.TYPE_STRING)

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
            return response.Response({'error': 'Activation Expired'}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError:
            return response.Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)

verEmail = VerifyEmail.as_view()
