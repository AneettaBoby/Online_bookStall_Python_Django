# Generated by Django 5.0.6 on 2024-08-14 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0038_cartdb_product_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckoutDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Email', models.EmailField(blank=True, max_length=100, null=True)),
                ('Address', models.EmailField(blank=True, max_length=100, null=True)),
                ('Phone', models.IntegerField(blank=True, null=True)),
                ('Totalprice', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]