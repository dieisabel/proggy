__all__ = ['password_reset_urlpatterns']


from django.urls import path

from django.contrib.auth import views as auth_views

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
