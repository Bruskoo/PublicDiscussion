from django.contrib import admin
from .models import Article, Comment

class ArticleAdmin(admin.ModelAdmin):
    search_fields = ['title', 'created_at', 'author']
    list_display = ('title', 'created_at')


class CommentAdmin(admin.ModelAdmin):
    search_fields = ['comment', 'author']

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
