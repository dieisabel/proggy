__all__ = ['DeleteBlogView']


from django.urls import reverse_lazy

from django.views.generic import DeleteView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from blog.models import Post


@method_decorator(login_required, name='dispatch')
class DeleteBlogView(DeleteView):
    model = Post
    template_name = 'blog/main/delete_blog.html'
    success_url = reverse_lazy('blog:blogs')
