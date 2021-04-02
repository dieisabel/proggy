__all__ = ['ProfileBioView']


from django.views.generic import DetailView
from django.contrib.auth.models import User


class ProfileBioView(DetailView):
    model = User
    template_name = 'accounts/main/profile/profile_bio.html'
    context_object_name = 'object'

    def get_object(self):
        return User.objects.get(username=self.get_username())

    def get_username(self):
        return self.kwargs.get('username')
