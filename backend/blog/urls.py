from django.urls import path

from . import views

urlpatterns = [
    path('', views.blogs, name='blog-blogs'),
    path('bloggers', views.bloggers, name='blog-bloggers'),
]
