__all__ = ['urlpatterns']


from django.urls import path
from django.urls import include
from django.contrib.auth import views as auth_views

from .views import RegisterView
from .views import ProfileBlogsView
from .views import ProfileBioView
from .views import ProfileEditView

app_name = 'accounts'

auth_urlpatterns = ([
    path('register', RegisterView.as_view(),
         name='register'),
    path('login',
         auth_views.LoginView.as_view(
             template_name='accounts/main/login.html'),
         name='login'),
    path('logout',
         auth_views.LogoutView.as_view(
             template_name='accounts/main/logout.html'),
         name='logout'),
], 'auth')

password_reset_urlpatterns = ([
    path('',
         auth_views.PasswordResetView.as_view(
             template_name='accounts/main/password_reset/initial.html'),
         name='initial'),
    path('done',
         auth_views.PasswordResetDoneView.as_view(
             template_name='accounts/main/password_reset/done.html'),
         name='done'),
    path('confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='accounts/main/password_reset/confirm.html'),
         name='confirm'),
    path('complete',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='accounts/main/password_reset/complete.html'),
         name='complete'),
], 'password_reset')

profile_urlpatterns = ([
    path('bio',
         ProfileBioView.as_view(),
         name='bio'),
    path('blogs',
         ProfileBlogsView.as_view(),
         name='blogs'),
    path('edit',
         ProfileEditView.as_view(),
         name='edit'),
], 'profile')

urlpatterns = [
    path('', include(auth_urlpatterns)),
    path('password-reset/', include(password_reset_urlpatterns)),
    path('profile/<str:username>/', include(profile_urlpatterns)),
]
