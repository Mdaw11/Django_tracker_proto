from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin

# Create your models here.
class User(AbstractUser, PermissionsMixin):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)
    
    avatar = models.ImageField(null=True, default="avatar.svg")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    

class user_type(models.Model):
    is_admin = models.BooleanField(default=False)
    is_developer = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        if self.is_developer == True:
            return User.get_email(self.user) + " - is_developer"
        else:
            return User.get_email(self.user) + " - is_admin"