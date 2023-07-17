# Generated by Django 4.2.1 on 2023-06-16 11:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('specialites', '0029_remove_specialites_users_specialites_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='specialites',
            name='users',
        ),
        migrations.AddField(
            model_name='specialites',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='specialites',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='specialites',
            name='updated_by',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='specialites',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='specialites',
            name='created_by',
            field=models.TextField(null=True),
        ),
    ]