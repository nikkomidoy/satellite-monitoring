from django.urls import path

from apps.monitoring.api.views import HealthCheckAPI, StatisticalDataAPI

urlpatterns = [
    path("health/", HealthCheckAPI.as_view(), name="api_health_check"),
    path("stats/", StatisticalDataAPI.as_view(), name="api_stats")
]
