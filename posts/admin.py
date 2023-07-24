from django.contrib import admin
from .models import Post
from . import models




class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'caption')

admin.site.register(Post, PostAdmin)
admin.site.register(models.Comment)
admin.site.register(models.Reply)
admin.site.register(models.Like)
admin.site.register(models.Like_comment)
