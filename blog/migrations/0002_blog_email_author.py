# Generated by Django 5.0 on 2023-12-23 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='email_author',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='автор статьи'),
        ),
    ]
