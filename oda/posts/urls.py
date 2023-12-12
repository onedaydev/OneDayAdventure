from django.urls import path
from posts.views import post_list, post_detail, post_add, post_modify, post_delete

app_name = "posts"
urlpatterns = [
    path("", post_list, name="post_list"),
    path("<int:post_id>/", post_detail, name="post_detail"),
    
    path("post_add/", post_add, name="post_add"),
    path("post_modify/", post_modify, name="post_modify"),
    path("post_delete/", post_delete, name="post_delete"),

    # path("comment_add/", comment_add, name="comment_add"),
    # path("comment_delete/<int:comment_id>/", comment_delete, name="comment_delete"),
]
