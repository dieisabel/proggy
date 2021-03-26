__all__ = ['profile_edit']


from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib import messages
from django.contrib.auth.decorators import login_required

from accounts.forms import UserUpdateForm
from accounts.forms import ProfileUpdateForm


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
