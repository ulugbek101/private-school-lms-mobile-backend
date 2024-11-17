from django.contrib.auth.models import UserManager

from .user_roles import UserTypes


class UserModelManager(UserManager):
    def create_user(self, email, first_name, last_name, password=None):
        """
        Create a regular user with the given email, name, and password.
        """
        if not email:
            raise ValueError("The Email field must be set")
        user = self.model(
            email=self.normalize_email(email),
            username=email.split("@")[0],
            first_name=first_name,
            last_name=last_name,
            role=UserTypes.STUDENT,  # Default role for regular users
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password):
        user = self.create_user(
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password,
        )
        user.role = "SUPERUSER"
        user.save(using=self._db)
        return user


class StudentManager(UserManager):
    def get_queryset(self):
        """
        Return a queryset filtered for students.
        """
        return super().get_queryset().filter(role="STUDENT")


class TeacherManager(UserManager):
    def get_queryset(self):
        """
        Return a queryset filtered for teachers.
        """
        return super().get_queryset().filter(role="TEACHER")


class AdminManager(UserManager):
    def get_queryset(self):
        """
        Return a queryset filtered for admins.
        """
        return super().get_queryset().filter(role="ADMIN")
