# Generated by Django 5.0 on 2023-12-23 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='название')),
                ('slug', models.CharField(blank=True, max_length=150, null=True, verbose_name='slug')),
                ('content', models.TextField(verbose_name='содержимое')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='previews/', verbose_name='изображение')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('is_published', models.BooleanField(default=False, verbose_name='признак публикации')),
                ('views_count', models.PositiveIntegerField(default=0, verbose_name='количество просмотров')),
            ],
            options={
                'verbose_name': 'запись',
                'verbose_name_plural': 'записи',
            },
        ),
    ]
