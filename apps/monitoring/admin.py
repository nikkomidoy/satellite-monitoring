from django.contrib import admin

from apps.monitoring.models import SatelliteData


@admin.register(SatelliteData)
class SatelliteDataAdmin(admin.ModelAdmin):
    readonly_fields = [
        "altitude",
        "last_updated",
        "created_at",
    ]
    list_display = [
        "altitude",
        "last_updated",
        "created_at",
    ]
    list_per_page = 20
    def has_add_permission(self, request):
        return False
