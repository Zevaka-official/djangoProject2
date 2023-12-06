from django.core.management.base import BaseCommand
from main.models import Category, Product


class Command(BaseCommand):
    help = 'Заполняет базу данных новыми данными, удаляя старые'

    def handle(self, *args, **kwargs):
        # Очистка данных
        Category.objects.all().delete()
        Product.objects.all().delete()

        # Заполнение новыми данными
        Category.objects.create(name='Новая категория', description='Описание новой категории')
        Product.objects.create(name='Новый продукт', description='Описание нового продукта', price=1000,
                               category=Category.objects.first())

        self.stdout.write(self.style.SUCCESS('База данных успешно заполнена новыми данными'))
