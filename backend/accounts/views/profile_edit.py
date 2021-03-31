__all__ = ['ProfileEditView']


from django.shortcuts import render
from django.shortcuts import redirect

from django.urls import reverse_lazy

from django.views.generic import View

from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from accounts.forms import UserUpdateForm
from accounts.forms import ProfileUpdateForm


@method_decorator(login_required, name='dispatch')
class ProfileEditView(View):
    template_name = 'accounts/main/profile/profile_edit.html'
    u_form = UserUpdateForm()
    p_form = ProfileUpdateForm()
    success_url = reverse_lazy('accounts-profile-bio')

    def get(self, request):
        context = {
            'forms': [self.u_form, self.p_form],
        }
        return render(request, self.template_name, context)

    def post(self, request):
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Account successfully updated!')
            return redirect(self.success_url)
        return self.get(request)
