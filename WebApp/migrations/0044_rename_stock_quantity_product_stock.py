# Generated by Django 5.0.6 on 2024-08-14 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0043_remove_product_stock_product_stock_quantity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='stock_quantity',
            new_name='stock',
        ),
    ]
