# Generated by Django 5.1 on 2024-10-01 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Budgeting', '0004_alter_sottocategoriaspesa_nome_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='transazione',
            name='eseguita',
            field=models.BooleanField(default=True),
        ),
    ]
