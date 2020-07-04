from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils import timezone
from django.contrib.auth.models import UserManager
from django.contrib.auth.models import BaseUserManager
class UserProfileManager(BaseUserManager):
    def create_user(self,email,password=None):
        if not email:
            raise ValueError('User must have an email address')
        user = self.model(email=self.normalize_email(email))

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self,email,password=None):
        if not email:
            return ValueError("email must not be empty")
        if not password:
            return ValueError("password must be provided")

        user = self.model(email=self.normalize_email(email))

        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user

# Create your models here.
class UserProfile(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = ['email']

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.email
class Post(models.Model):
    user = models.ForeignKey(UserProfile, related_name='posts', on_delete=models.CASCADE)
    titile = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    created_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titile
