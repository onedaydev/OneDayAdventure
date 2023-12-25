from django.shortcuts import render
from django.http import JsonResponse, Http404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView

from adventure.models import Adventure, Report
from adventure.tasks import adventure_background_tasks


class AdventureListView(LoginRequiredMixin, ListView):
    model = Adventure
    template_name = "adventure/adventure_list.html"
    context_object_name = "adventure"

    def get_queryset(self):
        return Adventure.objects.filter(user=self.request.user)


class AdventureDetailView(LoginRequiredMixin, DetailView):
    model = Adventure
    template_name = "adventure/adventure_detail.html"
    context_object_name = "adventure"

    def get_queryset(self):
        """현재 로그인한 사용자가 소유한 Adventure만 반환"""
        queryset = super().get_queryset()
        if not queryset.filter(user=self.request.user).exists():
            raise Http404("Adventure not found or access denied")
        return queryset.filter(user=self.request.user)


class AdventureCreateView(CreateView):
    model = Adventure
    fields = ["character_age", "character_class", "character_race"]
    template_name = "adventure/adventure_create.html"
    success_url = reverse_lazy("adventure:adventure_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        response = super().form_valid(form)

        user_id = self.request.user.id
        adventure_id = form.instance.id
        user_input = (
            form.instance.character_age,
            form.instance.character_class,
            form.instance.character_race,
        )

        adventure_background_tasks.delay(
            user_id=user_id, adventure_id=adventure_id, user_input=user_input
        )

        return response


class ReportListView(ListView):
    model = Report
    template_name = "adventure/report_list.html"
    context_object_name = "reports"

    def get_queryset(self):
        return Report.objects.filter(user=self.request.user)


class ReportDetailView(DetailView):
    model = Report
    template_name = "adventure/report_detail.html"
    context_object_name = "report"

    def get_queryset(self):
        """현재 로그인한 사용자가 소유한 Report만 반환"""
        queryset = super().get_queryset()
        if not queryset.filter(user=self.request.user).exists():
            raise Http404("Report not found or access denied")
        return queryset.filter(user=self.request.user)
