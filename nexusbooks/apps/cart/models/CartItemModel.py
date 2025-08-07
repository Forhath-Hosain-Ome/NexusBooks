from django.db import models
from .CartModel import Cart
from catalog.models import Book

class CartItem(models.Model):
    cart_item_id = models.CharField(primary_key=True, max_length=10)
    cart_id = models.ForeignKey(Cart, on_delete=models.SET_NULL)
    book_id = models.ForeignKey(Book, on_delete=models.SET_NULL)
    quantity = models.PositiveIntegerField()