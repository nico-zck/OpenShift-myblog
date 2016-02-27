from django.contrib import admin

from blog.models import *


# Register your models here.

class CommentInLine(admin.TabularInline):
    model = Comment
    extra = 1


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish_datetime', 'views_count')
    inlines = [CommentInLine]


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'comment', 'comment_datetime', 'article')


class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_datetime', 'message')


admin.site.register(Article, ArticleAdmin)
# admin.site.register(Comment, CommentAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Category)
admin.site.register(Tag)
