from django.db import models
from simple_history.models import HistoricalRecords


class Products(models.Model):
    name = models.CharField('Название продукта', max_length=25)
    company = models.CharField('Производитель', max_length=25)
    compound = models.TextField('Cостав продукта')
    amount = models.IntegerField('Количество')
    delivery = models.DateTimeField('Доставят к ', max_length=30)
    price = models.IntegerField('Цена')

    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Partners(models.Model):
    organization = models.CharField('Название компании', max_length=25)
    link = models.TextField('Ссылка на партнера ')
    reviews = models.IntegerField('Оценка компании')

    history = HistoricalRecords()

    def __str__(self):
        return self.organization

    class Meta:
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнеры'