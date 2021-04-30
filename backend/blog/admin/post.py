__all__ = ['PostAdmin']


from . import admin

from blog.models import Post
from .tabular import CommentInline


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'rating', 'created_at')
    list_display_links = ('title', 'author')
    list_filter = ('tags', 'created_at')
    search_fields = ('title',)
    readonly_fields = ('author', 'rating')
    inlines = (CommentInline,)
    save_on_top = True
    fields = (
        'title',
        'brief_description',
        'content',
        ('author', 'rating'),
    )
