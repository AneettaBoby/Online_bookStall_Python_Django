# Generated by Django 5.0.6 on 2024-06-26 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0002_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Category',
            field=models.CharField(default='exit', max_length=255),
            preserve_default=False,
        ),
    ]
