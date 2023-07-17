# Generated by Django 4.2 on 2023-05-16 08:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('consultations', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consultations',
            name='date',
        ),
        migrations.RemoveField(
            model_name='consultations',
            name='heure',
        ),
        migrations.AddField(
            model_name='consultations',
            name='cout',
            field=models.DecimalField(decimal_places=2, default=True, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='consultations',
            name='description',
            field=models.TextField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='consultations',
            name='libelle',
            field=models.CharField(default=True, max_length=255, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='consultations',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='consultations',
            name='updated_by',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='consultations',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='consultations',
            name='created_by',
            field=models.TextField(null=True),
        ),
    ]