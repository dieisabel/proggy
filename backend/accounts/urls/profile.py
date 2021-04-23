__all__ = ['profile_urlpatterns']


from django.urls import path

from ..views import ProfileBioView
from ..views import ProfileBlogsView
from ..views import ProfileEditView

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
