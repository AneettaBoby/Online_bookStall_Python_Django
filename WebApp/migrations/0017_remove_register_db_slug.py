# Generated by Django 5.0.6 on 2024-07-17 20:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0016_register_db_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register_db',
            name='slug',
        ),
    ]
