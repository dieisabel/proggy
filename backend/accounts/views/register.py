__all__ = ['register']


from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib import messages

from accounts.forms import UserRegistrationForm


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
