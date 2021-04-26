__all__ = ['ProfileEditView']


from django.shortcuts import render
from django.shortcuts import redirect

from django.views.generic import View

from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.models import User

from accounts.forms import UserUpdateForm
from accounts.forms import ProfileUpdateForm


class ProfileEditView(UserPassesTestMixin, View):
    template_name = 'accounts/main/profile/edit.html'

    def get(self, request, username):
        u_form = UserUpdateForm(instance=self.request.user)
        p_form = ProfileUpdateForm(instance=self.request.user.profile)
        context = {
            'forms': [u_form, p_form],
        }
        return render(request, self.template_name, context)

    def post(self, request, username):
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Account successfully updated!')
            return redirect('accounts:profile:bio', self.get_username())
        return self.get(request)

    def test_func(self):
        actual = self.request.user
        expected = User.objects.get(username=self.get_username())
        return actual == expected

    def get_username(self):
        return self.kwargs.get('username')
