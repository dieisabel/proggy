__all__ = ['CreditsView']


from django.views.generic import TemplateView


class CreditsView(TemplateView):
    template_name = 'blog/main/credits.html'
