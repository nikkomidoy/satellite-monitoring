from apps.monitoring.models import SatelliteData
from config import celery_app
from satellite_monitoring.utils.apis import SatelliteAPI

# NOTE: Try to move this to correct folder
@celery_app.task()
def get_satellite_data():
    """
    Returns the data coming from the satellite date endpoint
    """
    satellite_api = SatelliteAPI()
    data = satellite_api.get_current_altitude()

    try:
        SatelliteData.objects.create(**data)
    except:
        return "Data is not stored."

    return f"Altitude: {data.get('altitude')}, Last updated: {data.get('last_updated')}"
