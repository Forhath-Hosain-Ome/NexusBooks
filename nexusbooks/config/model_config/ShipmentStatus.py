from django.db.models import TextChoices

class ShipmentStatus(TextChoices):
    pending = 'Pending'
    shipped = 'Shipped'