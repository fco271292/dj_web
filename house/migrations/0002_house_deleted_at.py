# Generated by Django 4.2 on 2023-04-14 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='deleted_at',
            field=models.DateTimeField(null=True),
        ),
    ]
