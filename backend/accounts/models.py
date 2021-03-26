from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    GENDER_CHOICES = [
        ('F', 'Female'),
        ('M', 'Male'),
        ('?', 'Don\'t worry about it')
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField('аватарка',
                              default='default/default_profile_pic.png',
                              upload_to='profile_pics')
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        default='?')
    bio = models.TextField('биография', blank=True)
    birthday = models.DateField('день рождения', blank=True, null=True)
    twitter_url = models.URLField('твиттер', blank=True)
    custom_url = models.URLField('своя ссылка', blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    class Meta:
        db_table = 'profiles'
