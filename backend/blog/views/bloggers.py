__all__ = ['BloggersView']


from django.views.generic import ListView

from django.contrib.auth.models import User
from django.contrib.auth.models import Group


class BloggersView(ListView):
    model = User
    template_name = 'blog/main/bloggers.html'
    context_object_name = 'bloggers'

    def get_queryset(self):
        group_name = 'blogger'
        if not Group.objects.filter(name=group_name).exists():
            Group.objects.create(name=group_name)
        return Group.objects.get(name=group_name).user_set.all()

