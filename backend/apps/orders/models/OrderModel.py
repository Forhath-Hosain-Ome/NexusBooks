from django.db import models
from users.models import User
from config.model_config import ShipmentStatus

# Create your models here.
class Order(models.Model):
    order_id = models.CharField(primary_key=True, max_length=20)
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL)
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(decimal_places=2, max_length=5)
    status = models.CharField(choices=ShipmentStatus, default=ShipmentStatus.pending)
    shipping_address = models.CharField(max_length=50)
    promo_code = models.CharField(max_length=8)