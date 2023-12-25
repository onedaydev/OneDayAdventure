from django.contrib import admin
from adventure.models import Adventure, Report


class ReportInline(admin.TabularInline):
    model = Report


@admin.register(Adventure)
class AdventureAdmin(admin.ModelAdmin):
    pass
    # inlines = [
    #     ReportInline,
    # ]
    # list_display = []


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    # list_display = []
    pass
