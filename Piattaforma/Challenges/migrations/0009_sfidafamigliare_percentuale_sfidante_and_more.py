# Generated by Django 5.1 on 2024-10-11 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Challenges', '0008_alter_sfidafamigliare_descrizione'),
    ]

    operations = [
        migrations.AddField(
            model_name='sfidafamigliare',
            name='percentuale_sfidante',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='sfidafamigliare',
            name='percentuale_sfidato',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
