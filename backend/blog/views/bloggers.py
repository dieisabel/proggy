__all__ = ['BloggersView']


from django.views.generic import ListView

from django.contrib.auth.models import User
from django.contrib.auth.models import Group


class BloggersView(ListView):
    model = User
    template_name = 'blog/main/bloggers.html'
    context_object_name = 'bloggers'

    def get_queryset(self):
        return Group.objects.get(name='blogger').user_set.all()
