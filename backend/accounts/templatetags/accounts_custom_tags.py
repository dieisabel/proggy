__all__ = ['register', 'user_has_group']


from django import template

from utils import has_group

register = template.Library()


@register.filter(name='has_group')
def user_has_group(user, group):
    return has_group(user, group)
