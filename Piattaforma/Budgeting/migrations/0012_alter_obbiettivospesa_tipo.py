# Generated by Django 5.1 on 2024-10-08 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Budgeting', '0011_alter_transazione_tipo_rinnovo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='obbiettivospesa',
            name='tipo',
            field=models.CharField(choices=[('mensile', 'Monthly'), ('trimestrale', 'Quarterly'), ('semestrale', 'Semi-Annually'), ('annuale', 'Annually')], max_length=20),
        ),
    ]