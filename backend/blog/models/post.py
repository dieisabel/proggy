__all__ = ['Post']


from django.db import models
from django.urls import reverse

from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField('Заголовок', max_length=255)
    brief_description = models.CharField(
        'Краткое описание',
        max_length=1000,
        default=f'Cool blog, check it out!')
    content = models.TextField('Содержание')
    author = models.ForeignKey(
        User,
        verbose_name='Автор',
        on_delete=models.CASCADE)
    created_at = models.DateTimeField('Дата и время создания', auto_now_add=True)
    last_modified = models.DateTimeField('Последнее обновление', auto_now=True)
    rating = models.IntegerField('Рейтинг', default=0)
    tags = models.ManyToManyField('Tag', verbose_name='Теги')

    class Meta:
        db_table = 'posts'
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return f'{self.title} by {self.author}'

    def get_absolute_url(self):
        return reverse('blog:posts:post', kwargs={'pk': self.pk})
