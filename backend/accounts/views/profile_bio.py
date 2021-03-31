__all__ = ['ProfileBioView']


from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


@method_decorator(login_required, name='dispatch')
class ProfileBioView(TemplateView):
    template_name = 'accounts/main/profile/profile_bio.html'
