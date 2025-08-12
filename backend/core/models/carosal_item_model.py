from django.db import models

class CarosalItem(models.Model):
    title = models.CharField(max_length=15)
    message = models.CharField(max_length=20)