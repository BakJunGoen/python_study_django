# Generated by Django 4.1 on 2023-05-26 06:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("modules", "0002_remove_user_test2"),
    ]

    operations = [
        migrations.RemoveField(model_name="user", name="test",),
    ]
