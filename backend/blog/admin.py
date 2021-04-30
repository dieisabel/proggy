__all__ = ['CommentInline', 'PostAdmin', 'TagAdmin', 'CommentAdmin']


from django.contrib import admin

from .models import Post
from .models import Tag
from .models import Comment


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1
    readonly_fields = ('author',)


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


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    readonly_fields = ('author', 'post')
    fields = (
        'content',
        ('post', 'author'),
    )
