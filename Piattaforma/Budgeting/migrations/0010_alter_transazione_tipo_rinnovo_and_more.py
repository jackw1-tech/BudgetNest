# Generated by Django 5.1 on 2024-10-08 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Budgeting', '0009_obbiettivospesa_importo_speso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transazione',
            name='tipo_rinnovo',
            field=models.CharField(blank=True, choices=[('settimanale', 'Weekly Renewal'), ('mensile', 'Monthly Renewal'), ('semestrale', 'Semi-Annual Renewal')], default='settimanale', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='transazione',
            name='tipo_transazione',
            field=models.CharField(choices=[('delegata', 'Delegated Transaction'), ('singola', 'Single Transaction'), ('periodica', 'Recurring Transaction'), ('futura', 'Future Transaction'), ('trasferimento', 'Account Transfer'), ('investimento', 'Investment Transaction')], default='singola', max_length=20),
        ),
    ]
