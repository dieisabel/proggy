from django.urls import path

from . import views

urlpatterns = [
    path('', views.blogs),
    path('bloggers', views.bloggers),
    path('userpage', views.userpage)
]
