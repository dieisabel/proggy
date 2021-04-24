__all__ = ['Tag']


from django.db import models


class Tag(models.Model):

    name = models.CharField('Имя', max_length=50)

    class Meta:
        db_table = 'tags'
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name

