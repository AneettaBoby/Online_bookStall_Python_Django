# Generated by Django 5.0.6 on 2024-08-19 03:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChatApp', '0003_room_remove_groupmessage_group_and_more'),
        ('WebApp', '0046_checkoutdb_productname_checkoutdb_quantity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='message',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebApp.register_db'),
        ),
    ]
