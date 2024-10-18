# Generated by Django 5.1 on 2024-10-08 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0003_alter_utente_user_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utente',
            name='sesso',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='M', max_length=1),
        ),
    ]