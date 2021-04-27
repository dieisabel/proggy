__all__ = ['UpdateBlogView']

from django.views.generic import UpdateView
from django.contrib.auth.mixins import UserPassesTestMixin

from blog.models import Post


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
                or not self.request.user.groups.filter(name='blogger').exists():
            return False
        return True
