from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager



class UserManager(BaseUserManager):

    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")

        email = self.normalize_email(email)

        user = self.model(
            email=email,
            username=username,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, email, username, phone_number, password=None, **extra_fields):

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True")

        return self.create_user(
            email=email,
            username=username,
            password=password,
            phone_number=phone_number,
            **extra_fields
        )



   
class User(AbstractUser):
    email=models.EmailField(unique=True)
    phone_number=models.CharField(max_length=15,unique=True)

    profile_image=models.ImageField(upload_to="/profile_images",blank=True,null=True)

    is_email_verified=models.BooleanField(default=False)
    is_phone_verified=models.BooleanField(default=False)

    is_deleted=models.BooleanField(default=False)

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ["username", "phone_number"]

    def __str__(self):
        return self.username
    