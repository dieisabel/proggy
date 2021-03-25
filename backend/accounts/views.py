from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib.auth.decorators import login_required

from django.contrib import messages

from .forms import UserRegistrationForm
from .forms import UserUpdateForm
from .forms import ProfileUpdateForm


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created {username}')
            form.save()
            return redirect('blog-blogs')
    form = UserRegistrationForm()
    return render(request, 'accounts/main/registration.html', {'form': form})


@login_required
def profile_bio(request):
    return render(request, 'accounts/main/profile/profile_bio.html')


@login_required
def profile_blogs(request):
    return render(request, 'accounts/main/profile/profile_blogs.html')


@login_required
def profile_edit(request):
    u_form = UserUpdateForm()
    p_form = ProfileUpdateForm()
    if request.POST:
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Account successfully updated!')
            return redirect('accounts-profile-bio')
    context = {
        'forms': [u_form, p_form],
    }
    return render(request, 'accounts/main/profile/profile_edit.html', context)
