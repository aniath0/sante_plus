# Generated by Django 4.2 on 2023-05-16 08:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('roles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='roles',
            name='description',
            field=models.TextField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='roles',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='roles',
            name='updated_by',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='roles',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='roles',
            name='created_by',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='roles',
            name='libelle',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
