# Generated by Django 5.0.6 on 2024-07-09 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0009_alter_product_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register_db',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(blank=True, max_length=100, null=True)),
                ('Password', models.CharField(blank=True, max_length=100, null=True)),
                ('Confirm_password', models.CharField(blank=True, max_length=100, null=True)),
                ('Email', models.EmailField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
