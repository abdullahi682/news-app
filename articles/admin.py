from django.contrib import admin
from .models import Article, Comment

class CommentInline(admin.TabularInline):  # Changed to TabularInline
    model = Comment
    extra = 0  # To show no extra empty forms

class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]

# Register your models here.
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
