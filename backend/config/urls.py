from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin

from django.urls import path
from django.urls import include

from django.contrib.auth import views as auth_views

from accounts.views import register
from accounts.views import profile
from accounts.views import profile_blogs


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('register', register, name='accounts-register'),
    path('login',
         auth_views.LoginView.as_view(template_name='accounts/login.html'),
         name='accounts-login'),
    path('logout',
         auth_views.LogoutView.as_view(template_name='accounts/logout.html'),
         name='accounts-logout'),
    path('profile',
         profile, name='accounts-profile'),
    path('profile/blogs',
         profile_blogs, name='accounts-profile-blogs'),
]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
