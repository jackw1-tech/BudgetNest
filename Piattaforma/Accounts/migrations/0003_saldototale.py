# Generated by Django 5.1 on 2024-10-03 15:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0002_alter_conto_nome'),
        ('Users', '0003_alter_utente_user_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='SaldoTotale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saldo_totale', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('data_aggiornamento', models.DateField(auto_now=True)),
                ('utente', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Users.utente')),
            ],
        ),
    ]