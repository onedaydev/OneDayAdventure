from django.urls import path
from posts.views import (
    post_list,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    CommentCreateView,
    CommentDeleteView,
)

app_name = "posts"
urlpatterns = [
    path("", post_list, name="post_list"),
    path("<int:pk>/detail/", PostDetailView.as_view(), name="post_detail"),
    path("create/", PostCreateView.as_view(), name="post_create"),
    path("<int:pk>/update/", PostUpdateView.as_view(), name="post_update"),
    path("<int:pk>/delete/", PostDeleteView.as_view(), name="post_delete"),
    path("comment_add/", CommentCreateView.as_view(), name="comment_add"),
    path(
        "<int:pk>/comment_delete/", CommentDeleteView.as_view(), name="comment_delete"
    ),
]
