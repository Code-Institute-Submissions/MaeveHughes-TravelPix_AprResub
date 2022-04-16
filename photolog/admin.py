"""Options for admins page"""

from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment, Account, Friend


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """Admins post model features"""
    summernote_fields = ('content',)
    list_filter = ('status', 'created_on')
    list_display = ('title', 'author', 'status', 'created_on')
    search_fields = ['title', 'content', 'author']


admin.site.register(Account)
admin.site.register(Friend)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Admins post model features"""
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, queryset):
        """Approve comments"""
        queryset.update(approved=True)
