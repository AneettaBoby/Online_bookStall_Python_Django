# Generated by Django 5.0.6 on 2024-07-22 18:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChatApp', '0002_groupmessage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='groupmessage',
            name='group',
        ),
        migrations.RemoveField(
            model_name='groupmessage',
            name='author',
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=255)),
                ('message', models.TextField()),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ChatApp.room')),
            ],
        ),
        migrations.DeleteModel(
            name='ChatGroup',
        ),
        migrations.DeleteModel(
            name='GroupMessage',
        ),
    ]