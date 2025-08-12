from django.db.models import TextChoices

class discount_type(TextChoices):
    Percentage = 'Percentage'
    Fixed = 'Fixed'