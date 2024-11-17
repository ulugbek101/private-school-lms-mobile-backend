from django.db import models


class UserTypes(models.TextChoices):
    STUDENT = "STUDENT", "Student"
    TEACHER = "TEACHER", "Ustoz"
    ADMIN = "ADMIN", "Admin"
    SUPERUSER = "SUPERUSER", "Superadmin"
