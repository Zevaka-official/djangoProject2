# Generated by Django 4.2.7 on 2024-01-16 11:28

from django.db import migrations
import users_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', users_app.models.UserManager()),
            ],
        ),
    ]
