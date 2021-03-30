__all__ = ['BlogDetailView']


from django.views.generic import DetailView

from blog.models import Post


class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/main/blog.html'
    context_object_name = 'blog'
