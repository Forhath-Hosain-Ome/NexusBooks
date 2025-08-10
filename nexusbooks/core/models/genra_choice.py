from django.db.models import TextChoices

class GenraChoice(TextChoices):
    Classic = 'Classic'
    Kids = 'kids'
    Mature = 'Mature'
    Thrillers = 'Thrillers'
    Textbooks = 'Textbooks'