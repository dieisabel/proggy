__all__ = ['ProfileBlogsView']


from django.views.generic import View

from django.shortcuts import render

from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from blog.models import Post


class ProfileBlogsView(View):
    model = Post

    def get(self, request, username):
        user = self.get_user(username)
        context = {}
        if self.check_group(user):
            posts = self.get_posts(username)
            context.update({'object_list': posts})
            return render(
                request,
                'accounts/main/profile/blogs.html',
                context)
        context.update({'object': user})
        return render(
            request,
            'accounts/main/profile/not_blogger.html',
            context)

    def get_posts(self, username):
        return Post.objects.all(
            ).filter(author__username=username
            ).order_by('-created_at')

    def get_user(self, username):
        return User.objects.get(username=username)

    def check_group(self, user):
        group = Group.objects.get(name="blogger")
        return group.user_set.filter(username=user.username).exists()
