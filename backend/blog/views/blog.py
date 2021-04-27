__all__ = ['BlogDetailView']


from django.views.generic import DetailView

from django.shortcuts import redirect

from blog.models import Post
from blog.models import Comment
from blog.forms import CommentForm


class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/main/post_crud/post.html'
    context_object_name = 'blog'

    def post(self, request, pk):
        comment_form = CommentForm(self.request.POST)
        if comment_form.is_valid():
            Comment.objects.create(author=self.request.user,
                                   post=Post.objects.all().filter(id=pk).first(),
                                   content=comment_form.cleaned_data.get('comment_content'))
        return redirect('blog:posts:post', pk)
