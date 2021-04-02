__all__ = ['ProfileBlogsView']


from django.views.generic import ListView
from blog.models import Post


class ProfileBlogsView(ListView):
    model = Post
    template_name = 'accounts/main/profile/profile_blogs.html'

    def get_queryset(self):
        return Post.objects.all(
            ).filter(author__username=self.get_username()
            ).order_by('-created_at')

    def get_username(self):
        return self.kwargs.get('username')
