from django.urls import path

from . import views

urlpatterns = [
    path('', views.BlogsView.as_view(), name='blog-blogs'),
    path('create_blog', views.CreateBlogView.as_view(), name='blog-create-blog'),
    path('post/<int:pk>', views.BlogDetailView.as_view(), name='blog-blog'),
    path('bloggers', views.bloggers, name='blog-bloggers'),
]
