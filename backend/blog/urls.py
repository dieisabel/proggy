from django.urls import path

from . import views

urlpatterns = [
    path('', views.BlogsView.as_view(), name='blog-blogs'),
    path('bloggers', views.bloggers, name='blog-bloggers'),
]
