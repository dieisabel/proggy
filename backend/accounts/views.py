from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created {username}')
            form.save()
            return redirect('blog-blogs')
    form = UserCreationForm()
    return render(request, 'accounts/registration.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'accounts/profile.html')
