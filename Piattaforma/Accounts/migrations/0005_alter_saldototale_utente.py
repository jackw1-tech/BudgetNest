# Generated by Django 5.1 on 2024-10-03 16:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0004_alter_saldototale_data_aggiornamento'),
        ('Users', '0003_alter_utente_user_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saldototale',
            name='utente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.utente'),
        ),
    ]