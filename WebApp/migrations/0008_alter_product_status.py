# Generated by Django 5.0.6 on 2024-06-30 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0007_rename_product_image_product_productimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending', max_length=10),
        ),
    ]
