__all__ = ['BlogsView']


from django.views.generic import ListView

from blog.models import Post


class BlogsView(ListView):
    model = Post
    template_name = 'blog/main/blogs.html'
    context_object_name = 'blogs'
    ordering = ['-created_at']
