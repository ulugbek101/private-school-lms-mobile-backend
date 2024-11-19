from rest_framework import serializers

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import Subject


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
