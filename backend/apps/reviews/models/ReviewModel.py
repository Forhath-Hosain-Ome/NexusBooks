from django.db import models
from catalog.models import Book
from users.models import User

# Create your models here.
class Review(models.Model):
    review_id = models.CharField(max_length=20, primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL)
    book_id = models.ForeignKey(Book, on_delete=models.SET_NULL)
    rating = models.CharField(max_length=1)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
