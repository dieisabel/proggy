__all__ = ['has_group']


from django.contrib.auth.models import Group


def has_group(user, group):
    if not Group.objects.filter(name=group).exists():
        Group.objects.create(name=group)
    return user.groups.filter(name=group).exists()
