from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.paginator import Paginator
from django.http import HttpResponseForbidden

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
        posts = Post.objects.all().order_by('-id')

    paginator = Paginator(posts, 10)

    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
    }
    return render(request, "posts/post_list.html", context)


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "posts/post_create.html"
    success_url = reverse_lazy("posts:post_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

class PostDetailView(DetailView):
    model = Post
    template_name = "posts/post_detail.html"
    context_object_name = "post"


class PostUpdateView(UpdateView):
    pass


class PostDeleteView(UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'posts/post_delete.html'
    success_url = reverse_lazy('posts:post_list') 

    def test_func(self):
        return self.request.user == self.get_object().user
    
    def handle_no_permission(self):
        error_message = "삭제 권한이 없습니다"
        return HttpResponseForbidden(error_message)