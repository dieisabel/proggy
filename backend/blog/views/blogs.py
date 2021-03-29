__all__ = ['blogs']


from django.shortcuts import render

from blog.models import Post


def blogs(request):
    context = {
        "blogs": Post.objects.all(),
    }
    return render(request, 'blog/main/blogs.html', context)
