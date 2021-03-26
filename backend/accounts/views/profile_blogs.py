__all__ = ['profile_blogs']


from django.shortcuts import render

from django.contrib.auth.decorators import login_required


@login_required
def profile_blogs(request):
    return render(request, 'accounts/main/profile/profile_blogs.html')
