from django.contrib import admin
from .models import *


class StopsAdmin(admin.ModelAdmin):
    list_display = ("stop_id", "route_number", "city", "zip_code", "apt_plot", "scheduled_arrival_time",
                    "updated_at")


admin.site.register(Stops, StopsAdmin)


class SchoolAdmin(admin.ModelAdmin):
    list_display = ("id", "school_id", "stop_id", "school_name", "opening_time", "closing_time",
                    "updated_by", "created_by", "updated_at")


admin.site.register(School, SchoolAdmin)
