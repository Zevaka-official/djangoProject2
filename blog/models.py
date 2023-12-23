import pytils as pytils
from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    slug = models.CharField(max_length=150, null=True, blank=True, verbose_name='slug')
    content = models.TextField(verbose_name='содержимое')
    preview = models.ImageField(upload_to='previews/', null=True, blank=True, verbose_name='изображение')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    is_published = models.BooleanField(default=False, verbose_name='признак публикации')
    views_count = models.PositiveIntegerField(default=0, verbose_name='количество просмотров')
    email_author = models.EmailField(null=True, blank=True, verbose_name='автор статьи')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = pytils.translit.slugify(self.title)
        super().save(*args, **kwargs)


    class Meta:
        verbose_name = 'запись'
        verbose_name_plural = 'записи'
