# Generated by Django 2.2.24 on 2021-08-13 21:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('remplissages', '0002_person_whatsapp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evangelisation',
            name='site',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='evangelisations', to='remplissages.Site', verbose_name="Lieu d'évangelisation"),
        ),
    ]