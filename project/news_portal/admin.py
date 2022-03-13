from django.contrib import admin
from .models import Category, Post, PostCategory, Author

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(PostCategory)
admin.site.register(Author)
