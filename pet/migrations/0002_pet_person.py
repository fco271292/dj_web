# Generated by Django 4.2 on 2023-05-03 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0001_initial'),
        ('pet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='person',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='person.person'),
        ),
    ]