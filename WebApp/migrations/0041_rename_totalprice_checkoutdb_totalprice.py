# Generated by Django 5.0.6 on 2024-08-14 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0040_rename_totalprice_checkoutdb_totalprice'),
    ]

    operations = [
        migrations.RenameField(
            model_name='checkoutdb',
            old_name='TotalPrice',
            new_name='Totalprice',
        ),
    ]
