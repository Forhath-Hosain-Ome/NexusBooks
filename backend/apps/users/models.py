from django.db import models
from django.contrib.auth.models import AbstractUser
from config.model_config import RoleChoice
# Create your models here.

class User(AbstractUser):
    role = models.CharField(max_length=10, choices=RoleChoice, default=RoleChoice.Customer)
    