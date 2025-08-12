from django.db import models
from users.models import User

class Cart(models.Model):
    cart_id = models.CharField(primary_key=True, max_length=10)
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.CharField(max_length=2)