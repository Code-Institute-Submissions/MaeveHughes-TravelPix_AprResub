from django.contrib import admin
from .models import Account, Friend
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

admin.site.register(Account)
admin.site.register(Friend)
admin.site.register(Comment)
# Register your models here.
