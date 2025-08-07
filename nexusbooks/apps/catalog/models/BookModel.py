from django.db import models
from .CategoryModel import Category

# Create your models here.
class Book(models.Model):
    book_id = models.CharField(max_length=10, primary_key=True)
    isbn = models.CharField(max_length=13)
    title = models.CharField(max_length=40)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_length=5)
    stock_quantity = models.PositiveIntegerField()
    cover_url = models.ImageField(upload_to='{self.book_id}/')
    published_date = models.DateField()
    avg_rating = models.FloatField()
    category = models.ManyToManyField(Category, limit_choices_to=Category.name)