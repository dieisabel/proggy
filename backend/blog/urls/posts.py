__all__ = ['posts_urlpatterns']


from django.urls import path

import blog.views as views

posts_urlpatterns = ([
    path('',
         views.CreateBlogView.as_view(),
         name='create'),
    path('<int:pk>/update',
         views.UpdateBlogView.as_view(),
         name='update'),
    path('<int:pk>/delete',
         views.DeleteBlogView.as_view(),
         name='delete'),
    path('<int:pk>',
         views.BlogDetailView.as_view(),
         name='post'),
], 'posts')
