# Generated by Django 5.0 on 2023-12-14 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_contact_remove_category_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photos/', verbose_name='изображение'),
        ),
    ]