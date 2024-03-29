# Generated by Django 4.2.6 on 2023-10-20 17:31

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('d531d991-5d1a-4baa-805e-360cfeb43667'), primary_key=True, serialize=False)),
                ('number', models.CharField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(null=True)),
            ],
        ),
    ]
