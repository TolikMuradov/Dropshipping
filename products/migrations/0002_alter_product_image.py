# Generated by Django 5.2.1 on 2025-05-08 18:52

import products.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='products/', validators=[products.validators.validate_image]),
        ),
    ]
