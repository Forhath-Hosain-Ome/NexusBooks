from django.db.models import TextChoices

class discounttype(TextChoices):
    Percentage = 'Percentage'
    Fixed = 'Fixed'