# Generated by Django 5.1 on 2024-10-14 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0010_posizioneaperta_numero_azioni'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posizioneaperta',
            name='nome_azienda',
            field=models.CharField(max_length=50),
        ),
    ]
