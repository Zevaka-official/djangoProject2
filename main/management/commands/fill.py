from django.core.management import BaseCommand

from main.models import Product, Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()

        categories_list = [Category(name='Pepé Мемы', description='Мемы с Пепе'),
                           Category(name='Pepé Комиксы', description='Комиксы с Пепе'),
                           Category(name='Pepé Продукты', description='Продукты с изображением Пепе'),
                           ]

        Category.objects.bulk_create(categories_list)
        product_list = [Product(name='Пепе Футболка', description='Футболка с изображением Пепе', price=150,
                                category=categories_list[2]),
                        Product(name='Пепе Кружка', description='Футболка с изображением Пепе', price=150,
                                category=categories_list[2]),
                        Product(name='Пепе Memes', description='Мемы про Пепе', price=150,
                                category=categories_list[0]),
                        Product(name='Пепе Манго', description='Манго про Пепе', price=150,
                                category=categories_list[1]),
                        Product(name='Панамка с Пепе', description='Головной убор с Пепе', price=150,
                                category=categories_list[2]),
                        Product(name='Носки с Пепе', description='Носочки с Пепегой', price=150,
                                category=categories_list[2]),

                        ]

        Product.objects.bulk_create(product_list)
