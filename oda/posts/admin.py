from django.contrib import admin
from posts.models import Post, Comment, Announcement


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]
    list_display = [
        "title",
        "id",
        "user",
        "date",
    ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "post",
        "content",
        "date",
    ]

@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    pass