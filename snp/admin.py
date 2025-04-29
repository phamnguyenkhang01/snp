from django.contrib import admin

from .models import Post, Like, Comment, Friend

# Register your models here.
admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Comment)

class FriendAdmin(
    admin.ModelAdmin
):
    readonly_fields = ('requested_at',)
admin.site.register(Friend, FriendAdmin)


