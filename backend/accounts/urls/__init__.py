__all__ = ['urlpatterns']


from django.urls import path
from django.urls import include

from .auth import auth_urlpatterns
from .password_reset import password_reset_urlpatterns
from .profile import profile_urlpatterns

app_name = 'accounts'

urlpatterns = [
    path('', include(auth_urlpatterns)),
    path('password-reset/', include(password_reset_urlpatterns)),
    path('profile/<str:username>/', include(profile_urlpatterns)),
]
