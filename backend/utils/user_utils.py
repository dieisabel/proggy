__all__ = ['has_group']


def has_group(user, group):
    return user.groups.filter(name=group).exists()
