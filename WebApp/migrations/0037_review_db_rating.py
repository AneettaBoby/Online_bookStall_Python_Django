# Generated by Django 5.0.6 on 2024-08-13 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0036_rename_name_review_db_comment_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='review_db',
            name='Rating',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
