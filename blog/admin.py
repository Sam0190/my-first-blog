from django.contrib import admin
from .models import Post, Comment


class CommentInLine(admin.StackedInline):
    model = Comment
    extra = 0


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_date', 'published_date', ]
    inlines = [CommentInLine, ]


admin.site.register(Comment)
