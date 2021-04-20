__all__ = ['BlogsView']


from django.views.generic import ListView

from blog.models import Post


class BlogsView(ListView):
    model = Post
    template_name = 'blog/main/blogs.html'
    context_object_name = 'blogs'
    ordering = '-created_at'

    def get_queryset(self):
        tag_name = self.request.GET.get('tag_name') or None
        if tag_name:
            return Post.objects.all(
                ).filter(tags__name=tag_name
                ).order_by(self.ordering)
        return Post.objects.all(
            ).order_by(self.ordering)
