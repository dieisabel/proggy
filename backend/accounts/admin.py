__all__ = ['ProfileAdmin']


from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Main', {
            'fields': ('user', 'bio', 'image', 'get_image', 'gender', 'birthday')
        }),
        ('Contacts', {
            'fields': ('twitter_url', 'custom_url')
        }),
    )
    readonly_fields = ('user', 'get_image')

    def get_image(self, instance):
        return mark_safe(f'<img src="{instance.image.url}" width=100 height=100 >')

    get_image.short_description = 'Изображение'
