from django.contrib import admin

from .models import Author, Category, Post ,Comment

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display=('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')