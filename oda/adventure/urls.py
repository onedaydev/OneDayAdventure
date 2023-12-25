from django.urls import path

from adventure.views import (
    AdventureListView,
    AdventureCreateView,
    AdventureDetailView,
    ReportListView,
    ReportDetailView
)

app_name = "adventure"
urlpatterns = [
    path("", AdventureListView.as_view(), name="adventure_list"),
    path("<int:pk>/detail/", AdventureDetailView.as_view(), name="adventure_detail"),
    path("create/", AdventureCreateView.as_view(), name="adventure_create"),
    path("reports", ReportListView.as_view(), name="report_list"),
    path("<int:pk>/report/detail/", ReportDetailView.as_view(), name="report_detail"),
]
