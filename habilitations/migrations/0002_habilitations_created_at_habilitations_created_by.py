# Generated by Django 4.2 on 2023-05-10 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habilitations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='habilitations',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='habilitations',
            name='created_by',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
