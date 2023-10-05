from django.db import models


class ProductList(models.Model):
    title = models.CharField('Название', max_length=50)
    description = models.TextField('Описание', max_length=250)
    date = models.DateField('Дата добавления')
    author = models.CharField('Автор', max_length=50, default=None)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
