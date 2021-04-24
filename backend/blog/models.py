from django.db import models

from django.urls import reverse

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
    tags = models.ManyToManyField('Tag')

    class Meta:
        db_table = 'posts'

    def __str__(self):
        return f'{self.title} by {self.author}'

    def get_absolute_url(self):
        return reverse('blog:posts:post', kwargs={'pk': self.pk})


class Tag(models.Model):

    name = models.CharField('Имя', max_length=50)

    class Meta:
        db_table = 'tags'

    def __str__(self):
        return self.name


class Comment(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    class Meta:
        db_table = 'comments'
        ordering = ['-date']

    def __str__(self):
        return f'By {self.author} on {self.post}'
