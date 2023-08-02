from datetime import timedelta

from django.conf import settings
from django.db.models import Avg, Min, Max
from django.utils.timezone import localtime

from apps.monitoring.models import SatelliteData


def get_min_max_average_altitude(minutes=1):
    """
    Get the average altitude from the recorded data over the last minute
    """
    last_timeframe = localtime() - timedelta(minutes=minutes)
    altitudes = SatelliteData.objects.filter(created_at__gte=last_timeframe)
    stats = altitudes.aggregate(
        Avg('altitude'),
        Min('altitude'),
        Max('altitude'),
    )
    return stats


def check_altitude_status():
    """
    Returns a status message based on the threshold set for average altitude
    """
    stats = get_min_max_average_altitude()
    average_altitude = stats.get('altitude__avg')

    if average_altitude is None:
        return "Not enough data yet."

    if average_altitude < settings.AVERAGE_ALTITUDE_THRESHOLD:
        return settings.BELOW_THRESHOLD_STATUS_MESSAGE

    return settings.ABOVE_THRESHOLD_STATUS_MESSAGE


def get_statistical_data_based_on_altitudes():
    """
    Returns the statistical data of the satellite's altitude over the last 5 minutes
    """
    stats = get_min_max_average_altitude(minutes=5)
    return dict(
        minimum=stats.get('altitude__min'),
        maximum=stats.get('altitude__max'),
        average=stats.get('altitude__avg'),
    )
