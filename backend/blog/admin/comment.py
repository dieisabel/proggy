__all__ = ['CommentAdmin']


from . import admin

from blog.models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post')
    list_display_links = ('author', 'post')
    readonly_fields = ('author', 'post')
    fields = (
        'content',
        ('post', 'author'),
    )
