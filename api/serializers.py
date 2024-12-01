from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import Subject

User = get_user_model()


class UserTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token["email"] = user.email
        token["first_name"] = user.first_name
        token["last_name"] = user.last_name
        token["is_superuser"] = user.is_superuser
        token["is_teacher"] = user.is_teacher
        token["is_admin"] = user.is_admin
        token["is_student"] = user.is_student
        token["is_studying"] = user.is_studying
        token["phone_number"] = user.phone_number
        token["profile_image"] = user.profile_image.url
        token["role"] = user.role

        return token


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True, max_length=255, label="Password")
    password2 = serializers.CharField(write_only=True, max_length=255, label="Password confirmation")

    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'profile_image', 'phone_number', 'role', 'password1', 'password2']

    def validate(self, data):
        """
        Check that the two passwords match.
        """
        if data.get('password1') and data.get('password2'):
            if data['password1'] != data['password2']:
                raise serializers.ValidationError("The two password fields didn't match.")
        return data

    def create(self, validated_data):
        """
        Create a new user instance and hash the password.
        """
        password = validated_data.pop('password1')  # Get the password1 value
        user = User(**validated_data)
        user.set_password(password)  # Hash the password before saving
        user.save()
        return user
