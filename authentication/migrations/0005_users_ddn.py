# Generated by Django 4.2 on 2023-05-22 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_alter_users_telephone'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='ddn',
            field=models.DateField(null=True),
        ),
    ]
