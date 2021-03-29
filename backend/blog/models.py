from django.db import models

from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField('заголовок', max_length=255)
    brief_description = models.CharField(
        'краткое описание',
        max_length=1000,
        default=f'Learn about {title} in this post!')
    content = models.TextField('текст')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField('дата и время создания',
                                      auto_now_add=True)
    last_modified = models.DateTimeField('последнее обновление', auto_now=True)
    rating = models.IntegerField('рейтинг', default=0)

    class Meta:
        db_table = 'posts'
