from django.urls import path

from django.contrib.auth import views as auth_views

from accounts.views import RegisterView
from accounts.views import ProfileBioView
from accounts.views import ProfileBlogsView
from accounts.views import ProfileEditView

urlpatterns = [
    path('register', RegisterView.as_view(), name='accounts-register'),
    path('login',
         auth_views.LoginView.as_view(template_name='accounts/main/login.html'),
         name='accounts-login'),
    path('logout',
         auth_views.LogoutView.as_view(template_name='accounts/main/logout.html'),
         name='accounts-logout'),
    path('profile/bio',
         ProfileBioView.as_view(), name='accounts-profile-bio'),
    path('profile/blogs',
         ProfileBlogsView.as_view(), name='accounts-profile-blogs'),
    path('profile/edit',
         ProfileEditView.as_view(), name='accounts-profile-edit'),
]
