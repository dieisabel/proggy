from django.contrib import admin

from django.urls import path
from django.urls import include

from accounts.views import register


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('register', register, name='accounts-register')
]
