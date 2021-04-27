__all__ = ['UpdateBlogView']

from django.views.generic import UpdateView
from django.contrib.auth.mixins import UserPassesTestMixin

from blog.models import Post
from utils import has_group


class UpdateBlogView(UserPassesTestMixin, UpdateView):
    model = Post
    fields = [
        'title',
        'brief_description',
        'content',
        'tags',
    ]
    template_name = 'blog/main/post_crud/update_post.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        if self.get_object().author.username != self.request.user.username \
                or not has_group(self.request.user, 'blogger'):
            return False
        return True
