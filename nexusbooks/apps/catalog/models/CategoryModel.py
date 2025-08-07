from django.db import models


class Category(models.Model):
    category_id = models.CharField(max_length=25, primary_key=True)
    name = models.CharField(max_length=20)