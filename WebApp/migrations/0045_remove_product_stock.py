# Generated by Django 5.0.6 on 2024-08-14 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0044_rename_stock_quantity_product_stock'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='stock',
        ),
    ]
