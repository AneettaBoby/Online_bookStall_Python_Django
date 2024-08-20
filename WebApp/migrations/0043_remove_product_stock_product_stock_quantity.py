# Generated by Django 5.0.6 on 2024-08-14 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0042_product_stock'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='stock',
        ),
        migrations.AddField(
            model_name='product',
            name='stock_quantity',
            field=models.IntegerField(default=1),
        ),
    ]
