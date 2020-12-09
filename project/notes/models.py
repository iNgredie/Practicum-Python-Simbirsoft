from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """" Custom user model
    """
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['']
    email = models.EmailField(
        'email',
        unique=True
    )

    def __str__(self):
        return '%s' % self.email


class Note(models.Model):
    """" Note model
    """
    title = models.CharField(max_length=255)
    text = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return '%s' % self.title
