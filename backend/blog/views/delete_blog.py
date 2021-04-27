__all__ = ['DeleteBlogView']


from django.urls import reverse_lazy

from django.views.generic import DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin

from blog.models import Post
from utils import has_group


class DeleteBlogView(UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/main/post_crud/delete_post.html'
    success_url = reverse_lazy('blog:blogs')

    def test_func(self):
        if self.get_object().author.username != self.request.user.username \
                or not has_group(self.request.user, 'blogger'):
            return False
        return True
