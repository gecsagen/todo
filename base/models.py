from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    """Задача"""
    #  пользователь на основе стандартной модели пользователя
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Пользователь')
    title = models.CharField(max_length=200, verbose_name='Заголовок задачи')
    description = models.TextField(max_length=2000, verbose_name='Описание задачи', null=True, blank=True)
    complete = models.BooleanField(default=False, verbose_name='Отметить задачу как выполненную')
    create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        ordering = ['complete']
