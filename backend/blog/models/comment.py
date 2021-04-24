__all__ = ['Comment']


from django.db import models

from django.contrib.auth.models import User

from.post import Post


class Comment(models.Model):

    author = models.ForeignKey(
        User,
        verbose_name='Автор',
        on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post,
        verbose_name='Статья',
        on_delete=models.CASCADE)
    date = models.DateTimeField('Дата', auto_now_add=True)
    content = models.TextField('Содержание')

    class Meta:
        db_table = 'comments'
        ordering = ['-date']
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f'By {self.author} on {self.post}'
