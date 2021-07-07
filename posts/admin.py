from django.contrib import admin
from posts.models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('profile', 'title', 'photo')
    list_editable = ('title', 'photo')

    fieldsets = (
        ('Post', {
            'fields': ('user', 'profile', 'title', 'photo')
        }),
        ('Metadata', {
            'fields': (('created', 'modified'),),
        }),
    )

    readonly_fields = ('created', 'modified')