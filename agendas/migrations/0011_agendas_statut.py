# Generated by Django 4.2 on 2023-06-08 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('statut', '0003_alter_statut_libelle'),
        ('agendas', '0010_remove_agendas_medecins_agendas_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='agendas',
            name='statut',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='agendas', related_query_name='agenda', to='statut.statut'),
        ),
    ]
