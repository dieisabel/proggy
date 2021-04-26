__all__ = ['register', 'user_has_group']


from django import template


register = template.Library()


@register.filter(name='has_group')
def user_has_group(user, group):
    return user.groups.filter(name=group).exists()
