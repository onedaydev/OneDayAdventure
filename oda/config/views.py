from django.shortcuts import render
from django.views.generic import TemplateView
from posts.models import Post, Announcement
from adventure.models import Report

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_posts'] = Post.objects.all().order_by('-date')[:5]
        context['latest_reports'] = Report.objects.filter(user=self.request.user).order_by('-date')[:5]
        context['announcements'] = Announcement.objects.all().order_by('-date')[:5]
        return context
    

def comingsoon(request):
    return render(request, "comingsoon.html")


def page_not_found(request, exception):
    return render(request, 'errors/404.html', {})


def internal_server_error(request):
    return render(request, 'errors/500,html', {})
