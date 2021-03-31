__all__ = ['RegisterView']


from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib import messages

from accounts.forms import UserRegistrationForm


class RegisterView(CreateView):
    template_name = 'accounts/main/registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('blog-blogs')

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        messages.success(
            self.request,
            f'{username} account created successfully! Now you can log in!'
        )
        return super().form_valid(form)
