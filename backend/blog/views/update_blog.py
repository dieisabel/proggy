__all__ = ['UpdateBlogView']


from django.views.generic import UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from blog.models import Post


@method_decorator(login_required, name='dispatch')
class UpdateBlogView(UpdateView):
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

