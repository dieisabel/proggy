__all__ = ['CreateBlogView']


from django.views.generic import CreateView
from django.contrib.auth.mixins import UserPassesTestMixin

from blog.models import Post
from utils import has_group


class CreateBlogView(UserPassesTestMixin, CreateView):
    model = Post
    fields = [
        'title',
        'brief_description',
        'content',
        'tags',
    ]
    template_name = 'blog/main/post_crud/create_post.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        if not has_group(self.request.user, 'blogger'):
            return False
        return True
