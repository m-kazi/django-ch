# Generated by Django 5.0.7 on 2024-07-12 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peets', '0002_alter_coffeetypes_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='coffeetypes',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
