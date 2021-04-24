__all__ = ['CreateBlogView']


from django.views.generic import CreateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from blog.models import Post


@method_decorator(login_required, name='dispatch')
class CreateBlogView(CreateView):
    model = Post
    fields = [
        'title',
        'brief_description',
        'content',
        'tags',
    ]
    template_name = 'blog/main/create_post.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
