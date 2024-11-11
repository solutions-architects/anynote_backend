from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework import validators
import re

def validate_password(password):
    """Check password requirements"""
    if len(password) < 8:
        raise serializers.ValidationError(('Пароль должен содержать не менее 8 символов.'))
    if not re.search(r'\d', password):
        raise serializers.ValidationError(('Пароль должен содержать хотя бы одну цифру.'))
    if not re.search(r'[A-Z]', password):
        raise serializers.ValidationError(('Пароль должен содержать хотя бы одну заглавную букву.'))

class RegisterSerializer(serializers.ModelSerializer):
    """
    Serializer for registration

    Return json with username, email, first_name, last_name
    in case of successful registration
    """
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    email = serializers.EmailField(
        required=True,
        validators=[validators.UniqueValidator(queryset=get_user_model().objects.all())]
        )

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password', 'password2', "first_name", "last_name")


    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = get_user_model().objects.create(
            username=validated_data.get('username'),
            first_name=validated_data.get('first_name', ""),
            last_name=validated_data.get('last_name', ""),
            email=validated_data.get('email', ""),
        )

        user.set_password(validated_data['password'])
        user.save()

        return user

class EmailVerificationSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=555)
    class Meta:
        model = get_user_model()
        fields = ['token']
