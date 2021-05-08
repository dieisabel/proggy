__all__ = ['urlpatterns']


from django.urls import path
from django.urls import include

import blog.views as views

app_name = 'blog'

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

urlpatterns = [
    path('about', views.AboutView.as_view(), name='about'),
    path('credits', views.CreditsView.as_view(), name='credits'),
    path('contact', views.ContactView.as_view(), name='contact'),
    path('', views.BlogsView.as_view(), name='blogs'),
    path('bloggers', views.BloggersView.as_view(), name='bloggers'),
    path('posts/', include(posts_urlpatterns)),
]
