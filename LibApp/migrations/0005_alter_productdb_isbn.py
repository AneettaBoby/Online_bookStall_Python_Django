# Generated by Django 5.0.6 on 2024-06-17 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LibApp', '0004_productdb_author_productdb_genre_productdb_isbn_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdb',
            name='ISBN',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
