from django.contrib import admin

from django.urls import path
from django.urls import include

from django.contrib.auth import views as auth_views

from accounts.views import register


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('register', register, name='accounts-register'),
    path('login',
         auth_views.LoginView.as_view(template_name='accounts/login.html'),
         name='accounts-login'),
]
