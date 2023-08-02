from rest_framework.views import APIView
from rest_framework.response import Response

from satellite_monitoring.utils.calculations import check_altitude_status, get_statistical_data_based_on_altitudes


class HealthCheckAPI(APIView):
    """
    Check the status of the average altitude of Satellite
    """
    def get(self, request, format=None):
        return Response(
            dict(message=check_altitude_status())
        )


class StatisticalDataAPI(APIView):
    """
    Statistical data of the satellite's altitude over the last 5 minutes
    """
    def get(self, request, format=None):
        data = get_statistical_data_based_on_altitudes()
        return Response(
            dict(
                minimum=data.get('minimum'),
                maximum=data.get('maximum'),
                average=data.get('average'),
            )
        )
