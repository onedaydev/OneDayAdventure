from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from django.core.paginator import Paginator
from posts.models import Post
from posts.forms import PostForm


def post_list(request):
    page_number = request.GET.get("page")

    search = request.GET.get("search")

    if not page_number:
        page_number = 1

    if search:
        pass
    else:
        posts = Post.objects.all()

    paginator = Paginator(posts, 10)

    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
    }
    return render(request, "posts/post_list.html", context)


class create_post(CreateView):
    model = Post
    form_class = PostForm
    template_name = "posts/create_post.html"
    success_url = reverse_lazy("posts:post_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

class post_detail(DetailView):
    model = Post
    template_name = "posts/post_detail.html"
    contenxt_object_name = "post"

def post_modify(request):
    pass


def post_delete(request):
    pass
