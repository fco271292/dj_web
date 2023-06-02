from django.db import models

from person.models import Person


# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=255)

    person = models.ManyToManyField(Person, blank=True)

    class Meta:
        db_table = 'car'