from django.db.models import TextChoices

class RoleChoice(TextChoices):
    Customer = 'Customer'
    Admin = 'Admin'