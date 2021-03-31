from django.urls import path

from django.contrib.auth import views as auth_views

from accounts.views import RegisterView
from accounts.views import profile_bio
from accounts.views import ProfileBlogsView
from accounts.views import profile_edit

urlpatterns = [
    path('register', RegisterView.as_view(), name='accounts-register'),
    path('login',
         auth_views.LoginView.as_view(template_name='accounts/main/login.html'),
         name='accounts-login'),
    path('logout',
         auth_views.LogoutView.as_view(template_name='accounts/main/logout.html'),
         name='accounts-logout'),
    path('profile/bio',
         profile_bio, name='accounts-profile-bio'),
    path('profile/blogs',
         ProfileBlogsView.as_view(), name='accounts-profile-blogs'),
    path('profile/edit',
         profile_edit, name='accounts-profile-edit'),
]
