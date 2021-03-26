from django.db import models

class Prikaz(models.Model):
    number = models.CharField(max_length=10, verbose_name='Номер приказа')
    date = models.DateField(verbose_name='Дата приказа')
    name = models.CharField(max_length=200, verbose_name='Название')
    file = models.FileField(verbose_name='Файл')
    note = models.CharField(max_length=120, verbose_name='Примечание', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Приказ'
        verbose_name_plural = 'Приказы'



