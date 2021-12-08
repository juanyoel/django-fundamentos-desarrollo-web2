from django.contrib import admin
from .models import Post, PostView, Comments, Like

# Register your models here.
admin.site.register(Post)
admin.site.register(PostView)
admin.site.register(Comments)
admin.site.register(Like)

