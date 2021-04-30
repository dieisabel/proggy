__all__ = ['CommentInline']


from . import admin

from blog.models import Comment


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1
    readonly_fields = ('author',)
