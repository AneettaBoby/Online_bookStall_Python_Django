# Generated by Django 5.0.6 on 2024-07-12 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0013_alter_register_db_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register_db',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
