__all__ = ['ProfileBlogsView']


from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from blog.models import Post


class ProfileBlogsView(ListView):
    model = Post
    template_name = 'accounts/main/profile/profile_blogs.html'

    def get_queryset(self):
        return Post.objects.all(
            ).filter(author=self.request.user
            ).order_by('-created_at')
