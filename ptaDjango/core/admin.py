from django.contrib import admin
from .models import Post

class PostsAdmin(admin.ModelAdmin):
    list_display =('title', 'author', 'created_date')

# Register your models here.
admin.site.register(Post, PostsAdmin)