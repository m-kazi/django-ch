# Generated by Django 5.0.7 on 2024-07-12 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coffeetypes',
            name='type',
            field=models.CharField(choices=[('BLK', 'BLACK'), ('CUP', 'CUPPUCCINO'), ('MOC', 'MOCHA'), ('CBN', 'COFFEE_BEANS')], default='BLK', max_length=3),
        ),
    ]
