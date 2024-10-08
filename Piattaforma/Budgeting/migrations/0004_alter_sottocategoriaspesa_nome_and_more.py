# Generated by Django 5.1 on 2024-10-01 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Budgeting', '0003_alter_transazione_tipo_rinnovo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sottocategoriaspesa',
            name='nome',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='transazione',
            name='tipo_rinnovo',
            field=models.CharField(blank=True, choices=[('settimanale', 'Rinnovo Settimanale'), ('mensile', 'Rinnovo Mensile'), ('semestrale', 'Rinnovo Semestrale'), ('nessuno', 'Nessun Rinnovo')], default='nessuno', max_length=20, null=True),
        ),
    ]
