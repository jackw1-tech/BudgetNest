# Generated by Django 5.1 on 2024-10-11 11:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Challenges', '0004_sfidafamigliare_famiglia'),
        ('Users', '0006_remove_utente_famiglia_utente_famiglia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sfidafamigliare',
            name='famiglia',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Users.famiglia'),
        ),
    ]
