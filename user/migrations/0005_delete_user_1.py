# Generated by Django 4.1.4 on 2023-01-11 09:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_rename_user_user_1'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User_1',
        ),
    ]