import re

from django.contrib.auth import get_user_model

from rest_framework import serializers, validators
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

def validate_password(password):
    """Check password requirements"""
    if len(password) < 8:
        raise serializers.ValidationError(("Password should be at least 8 characters long"))
    if not re.search(r"\d", password):
        raise serializers.ValidationError(("Password should contain at least 1 number"))
    if not re.search(r"[A-Z]", password):
        raise serializers.ValidationError(("Password should contain at least 1 capital letter"))


class RegisterSerializer(serializers.ModelSerializer):
    """
    Serializer for registration

    Return json with username, email, first_name, last_name
    in case of successful registration
    """

    password = serializers.CharField(
        write_only=True, 
        required=True, 
        validators=[validate_password]
    )
    email = serializers.EmailField(
        required=True, 
        validators=[validators.UniqueValidator(queryset=get_user_model().objects.all())]
    )

    class Meta:
        model = get_user_model()
        fields = ("username", "email", "password")

    def validate(self, attrs):
        return attrs

    def create(self, validated_data):
        user = get_user_model().objects.create(
            username=validated_data.get("username"),
            email=validated_data.get("email", ""),
        )

        user.set_password(validated_data["password"])
        user.save()

        return user

class EmailVerificationSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=555)

    class Meta:
        model = get_user_model()
        fields = ["token"]


class EmailTokenObtainSerializer(TokenObtainPairSerializer):
    username_field = get_user_model().EMAIL_FIELD
