# Generated by Django 4.2.6 on 2023-10-20 17:42

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('phone', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='id',
            field=models.UUIDField(default=uuid.UUID('32905265-0865-4c89-8579-deb25b8d655b'), primary_key=True, serialize=False),
        ),
        migrations.AlterModelTable(
            name='phone',
            table='phone',
        ),
    ]
