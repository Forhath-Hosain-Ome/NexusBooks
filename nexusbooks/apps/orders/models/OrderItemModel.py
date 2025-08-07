from django.db import models
from .OrderModel import Order
from catalog.models import Book

class OrderItem(models.Model):
    order_item_id = models.CharField(max_length=20, primary_key=True)
    order_id = models.ManyToOneRel(Order, on_delete=models.SET_NULL)
    book_id = models.ManyToOneRel(Book, on_delete=models.SET_NULL)
    quantity = models.PositiveIntegerField()
    unit_price_at_order = models.DecimalField(decimal_places=2, max_length=6)