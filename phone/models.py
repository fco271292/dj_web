import uuid

from django.db import models
from django.db.models import Model


# Create your models here.
class Phone(Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=True)
    number = models.CharField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)

    class Meta:
        db_table = 'phone'
        ordering = ['-created_at']