# Generated by Django 4.2 on 2023-05-16 08:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('consultations', '0002_remove_consultations_date_remove_consultations_heure_and_more'),
        ('dossierpatients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consultationpatients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observation', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.TextField(null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.TextField(null=True)),
                ('consultations', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='consultationpatients', related_query_name='consultationpatient', to='consultations.consultations')),
                ('dossierpatients', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='consultationpatients', related_query_name='consultationpatient', to='dossierpatients.dossierpatients')),
            ],
        ),
    ]
