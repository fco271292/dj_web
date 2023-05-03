# Create your models here.
from datetime import datetime

from django.db import models

from person.models import Person


class House (models.Model):

    name = models.CharField(max_length=255, null=True)
    free = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)

    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'house'
