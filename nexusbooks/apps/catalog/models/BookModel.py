from django.db import models
from .CategoryModel import Category
# from config.internal_routing import media_upload_path



def media_upload_path(instance, filename):
    # Use book_id if already set, or use 'temp' as fallback
    folder_name = instance.book_id if instance.book_id else 'temp'
    return f'covers/{folder_name}/{filename}'


# Create your models here.
class Book(models.Model):
    book_id = models.CharField(max_length=10, primary_key=True)
    isbn = models.CharField(max_length=13)
    title = models.CharField(max_length=40)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=5)
    stock_quantity = models.PositiveIntegerField()
    cover_url = models.ImageField(upload_to=media_upload_path)
    published_date = models.DateField()
    avg_rating = models.FloatField()
    category = models.ManyToManyField(Category)