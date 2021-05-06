__all__ = ['urlpatterns']


from django.urls import path
from django.urls import include

import blog.views as views
from .posts import posts_urlpatterns

app_name = 'blog'

urlpatterns = [
    path('about', views.AboutView.as_view(), name='about'),
    path('credits', views.CreditsView.as_view(), name='credits'),
    path('contact', views.ContactView.as_view(), name='contact'),
    path('', views.BlogsView.as_view(), name='blogs'),
    path('bloggers', views.BloggersView.as_view(), name='bloggers'),
    path('posts/', include(posts_urlpatterns)),
]
