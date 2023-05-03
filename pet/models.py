from django.db import models

from person.models import Person


# Create your models here.
class Pet(models.Model):
    name = models.CharField(max_length=255)

    person = models.OneToOneField(Person, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'pet'
