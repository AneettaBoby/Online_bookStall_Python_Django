# Generated by Django 5.0.6 on 2024-07-05 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LibApp', '0007_remove_productdb_isbn'),
    ]

    operations = [
        migrations.AddField(
            model_name='productdb',
            name='status',
            field=models.CharField(default='approve', max_length=7),
        ),
    ]
