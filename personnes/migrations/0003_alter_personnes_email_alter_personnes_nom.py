# Generated by Django 4.2 on 2023-05-22 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personnes', '0002_alter_personnes_nom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personnes',
            name='email',
            field=models.EmailField(max_length=255),
        ),
        migrations.AlterField(
            model_name='personnes',
            name='nom',
            field=models.CharField(max_length=255),
        ),
    ]