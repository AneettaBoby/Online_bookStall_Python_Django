# Generated by Django 5.0.6 on 2024-08-14 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0039_checkoutdb'),
    ]

    operations = [
        migrations.RenameField(
            model_name='checkoutdb',
            old_name='Totalprice',
            new_name='TotalPrice',
        ),
    ]