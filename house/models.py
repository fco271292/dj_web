# Create your models here.
from datetime import datetime

from django.db import models

class House (models.Model):

    name = models.CharField(max_length=255, null=True)
    free = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)

    class Meta:
        db_table = 'house'
