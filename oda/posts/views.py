from typing import Any
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.paginator import Paginator
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.db.models.query_utils import Q
from django.views.decorators.http import require_POST

from posts.models import Post, Comment
from posts.forms import PostForm, CommentForm


def post_list(request):
    page_number = request.GET.get("page")
    search = request.GET.get("search")

    if not page_number:
        page_number = 1

    if search:
        posts = Post.objects.filter(
            Q(title__icontains=search) | Q(content__icontains=search)
        ).order_by("-id")
    else:
        posts = Post.objects.all().order_by("-id")

    paginator = Paginator(posts, 10)
    page_obj = paginator.get_page(page_number)

    if not search:
        search = ""

    context = {
        "page_obj": page_obj,
        "search": search,
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
    paginate_comments_by = 3

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["comment_form"] = CommentForm()

        comments_list = Comment.objects.filter(post=self.object)
        paginator = Paginator(comments_list, self.paginate_comments_by)

        page = self.request.GET.get('page')
        if not page:
            page = 1


        comments = paginator.get_page(page)

        
        context['comments'] = comments

        return context


class PostUpdateView(UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = "posts/post_update.html"

    def get_success_url(self):
        return reverse_lazy("posts:post_detail", kwargs={"pk": self.object.pk})

    def test_func(self):
        return self.request.user == self.get_object().user

    def handle_no_permission(self):
        error_message = "수정 권한이 없습니다"
        return HttpResponseForbidden(error_message)


class PostDeleteView(UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "posts/post_delete.html"
    success_url = reverse_lazy("posts:post_list")

    def test_func(self):
        return self.request.user == self.get_object().user

    def handle_no_permission(self):
        error_message = "삭제 권한이 없습니다"
        return HttpResponseForbidden(error_message)


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    # success_url = reverse_lazy("posts:post_detail", kwargs={"pk": })

    def get_success_url(self):
        return reverse_lazy("posts:post_detail", kwargs={"pk": self.object.post.pk})

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


# @require_POST
# def comment_add(request):
#     form = CommentForm(data=request.POST)
#     if form.is_valid():
#         comment = form.save(commit=False)
#         comment.user = request.user
#         comment.save()

#         return HttpResponseRedirect(f"../{request.POST.get('post')}/detail")
#     else:
#         error_message = "폼 에러"
#         return HttpResponseForbidden(error_message)


class CommentDeleteView(UserPassesTestMixin, DeleteView):
    model = Comment

    def get_success_url(self):
        return reverse_lazy("posts:post_detail", kwargs={"pk": self.object.post.pk})

    def test_func(self):
        return self.request.user == self.get_object().user

    def handle_no_permission(self):
        error_message = "삭제 권한이 없습니다"
        return HttpResponseForbidden(error_message)
