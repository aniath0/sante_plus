# Generated by Django 4.2 on 2023-05-19 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dossierpatients', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dossierpatients',
            name='numero',
            field=models.CharField(max_length=255),
        ),
    ]
