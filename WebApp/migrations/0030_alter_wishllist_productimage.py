# Generated by Django 5.0.6 on 2024-08-06 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0029_alter_wishllist_productimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishllist',
            name='ProductImage',
            field=models.ImageField(blank=True, null=True, upload_to='Pro_image/Product_Image'),
        ),
    ]
