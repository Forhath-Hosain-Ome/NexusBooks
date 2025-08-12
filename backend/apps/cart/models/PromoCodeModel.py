from django.db import models
from config.model_config import discount_type

class PromoCode(models.Model):
    code = models.CharField(primary_key=True, max_length=20)
    discount_type = models.CharField(choices=discount_type)
    discount_value = models.CharField(max_length=10)
    valid_from = models.DateTimeField()
    valid_until = models.DateTimeField()
    max_uses = models.PositiveIntegerField()