__all__ = ['profile_bio']


from django.shortcuts import render

from django.contrib.auth.decorators import login_required


@login_required
def profile_bio(request):
    return render(request, 'accounts/main/profile/profile_bio.html')
