# Generated by Django 5.0.6 on 2024-08-10 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0033_rename_price_wishllist_product_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishllist',
            name='Username',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
