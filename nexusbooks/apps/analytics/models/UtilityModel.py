from django.db import models
from config.internal_routing import UploadToFolder

class Utility(models.Model):
    logo = models.ImageField(upload_to=UploadToFolder('logo'))
    banner = models.ImageField(upload_to=UploadToFolder('banner'))