from django.shortcuts import render
from posts.models import Post


def post_list(request):
    posts = Post.objects.all()
    context = {
        "posts": posts,
    }
    return render(request, "posts/post_list.html", context)

def post_detail(request):
    pass


def post_add(request):
    pass


def post_modify(request):
    pass


def post_delete(request):
    pass
