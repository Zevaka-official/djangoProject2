from django.db import models

from djangoProject2 import settings

NULLABLE = {
    'null': True, 'blank': True
}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(max_length=1000, **NULLABLE, verbose_name='описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class ProductVersion(models.Model):
    version_name = models.CharField(max_length=255, verbose_name='версия')
    version_number = models.IntegerField(default=1, verbose_name='номер версии')
    is_latest = models.BooleanField(default=False, verbose_name='активная версия')
    product = models.ForeignKey('Product', related_name='versions', on_delete=models.CASCADE, verbose_name='товар')

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'

    def __str__(self):
        return self.version_name


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='наименование')
    description = models.TextField(max_length=2200, **NULLABLE, verbose_name='описание')
    photo = models.ImageField(upload_to='photos/', **NULLABLE, verbose_name='изображение')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='цена', default=0.0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='дата обновления')
    version = models.ForeignKey(ProductVersion, on_delete=models.SET_NULL, null=True, default=None,
                                related_name='products', verbose_name='версия')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='владелец')
    is_published = models.BooleanField(default=False, verbose_name='публиковано')

    @property
    def active_version(self):
        return self.versions.filter(is_latest=True).first()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        permissions = [
            (
                'set_published',
                'Can publish products'
            ),
        ]


class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    address = models.CharField(max_length=255, verbose_name='адрес')
    phone = models.CharField(max_length=100, verbose_name='телефон')
    email = models.EmailField(verbose_name='email')

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.cleaned_data = None

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'
