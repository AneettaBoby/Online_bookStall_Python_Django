# Generated by Django 5.0.6 on 2024-08-10 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0034_wishllist_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartdb',
            name='WishList',
        ),
    ]
