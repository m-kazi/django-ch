# Generated by Django 5.0.7 on 2024-07-12 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peets', '0004_coffeetypes_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coffeetypes',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
