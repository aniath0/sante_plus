# Generated by Django 4.2.1 on 2023-05-24 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('specialites', '0017_remove_specialites_users_specialites_description_and_more'),
        ('statut', '0003_alter_statut_libelle'),
        ('agendas', '0009_remove_agendas_personnes'),
        ('personnes', '0005_alter_personnes_telephone'),
        ('rendezvous', '0005_alter_rendezvous_agendas_alter_rendezvous_personnes_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rendezvous',
            name='agendas',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rendezvous', related_query_name='rendezvous', to='agendas.agendas'),
        ),
        migrations.AlterField(
            model_name='rendezvous',
            name='personnes',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rendezvous', related_query_name='rendezvous', to='personnes.personnes'),
        ),
        migrations.AlterField(
            model_name='rendezvous',
            name='specialites',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rendezvous', related_query_name='rendezvous', to='specialites.specialites'),
        ),
        migrations.AlterField(
            model_name='rendezvous',
            name='statut',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rendezvous', related_query_name='rendezvous', to='statut.statut'),
        ),
    ]
