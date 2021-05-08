__all__ = ['Profile']


from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):

    GENDER_CHOICES = [
        ('F', 'Female'),
        ('M', 'Male'),
        ('?', 'Don\'t worry about it')
    ]
    user = models.OneToOneField(
        User,
        verbose_name='Пользователь',
        on_delete=models.CASCADE)
    image = models.ImageField(
        verbose_name='Аватарка',
        default='default/default_profile_pic.png',
        upload_to='profile_pics')
    gender = models.CharField(
        verbose_name='Пол',
        max_length=1,
        choices=GENDER_CHOICES,
        default='?')
    bio = models.TextField('Биография', blank=True)
    birthday = models.DateField('День рождения', blank=True, null=True)
    twitter_url = models.URLField('Твиттер', blank=True)
    custom_url = models.URLField('Своя ссылка', blank=True)

    class Meta:
        db_table = 'profiles'
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return f'{self.user.username} Profile'
