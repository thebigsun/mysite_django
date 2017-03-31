from django.contrib import admin

# Register your models here.
from blog.models import BlogsPost, BlogPostAdmin

admin.site.register(BlogsPost,BlogPostAdmin)
