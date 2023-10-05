from django.db import models


class Users(models.Model):
    name = models.CharField('Имя', max_length=20)
    password = models.CharField('Пароль', max_length=50)
    phone = models.CharField('Номер телефона', max_length=12)
    TYPE_SELECT = (
        ('0', 'Производитель'),
        ('1', 'Покупатель'),
    )
    role = models.CharField('Роль', max_length=30, choices=TYPE_SELECT)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
