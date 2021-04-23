from django.urls import path, reverse_lazy

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
    path('profile/<str:username>/bio',
         ProfileBioView.as_view(), name='accounts-profile-bio'),
    path('profile/<str:username>/blogs',
         ProfileBlogsView.as_view(), name='accounts-profile-blogs'),
    path('profile/<str:username>/edit',
         ProfileEditView.as_view(), name='accounts-profile-edit'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
            template_name='accounts/main/password_reset.html'),
         name='password_reset'),
    path('password-reset/done',
         auth_views.PasswordResetDoneView.as_view(template_name='accounts/main/password_reset_done.html'),
         name='password_reset_done'),
    path('password_reset/confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='accounts/main/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password_reset/complete',
         auth_views.PasswordResetCompleteView.as_view(template_name='accounts/main/password_reset_complete.html'),
         name='password_reset_complete'),
]
