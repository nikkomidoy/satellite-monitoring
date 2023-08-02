import requests
from urllib.parse import urljoin
from django.conf import settings


class SatelliteAPI:
    def __init__(self):
        self.auth_endpoint = settings.SATELLITE_DATA_ENDPOINT

    def _perform_http_request(self, url, method):
        return requests.request(method=method, url=url, timeout=60)

    def _request(self, endpoint, url_suffix, method='get'):
        url = urljoin(endpoint, url_suffix)
        api_http_response = self._perform_http_request(url=url, method=method)
        api_headers_response = api_http_response.headers
        api_json_response = api_http_response.json() if api_http_response.content else None
        return api_headers_response, api_json_response, api_http_response.status_code

    def _create_request(self):
        headers, response, status_code = self._request(
            endpoint=self.auth_endpoint,
            url_suffix="",
        )
        return dict(
            headers=headers,
            response=response,
            status_code=status_code,
        )

    def get_current_altitude(self):
        """
        Gets the current altitude based on the satellite data
        """
        api = self._create_request()
        response = api.get('response')
        return dict(
            altitude=response.get('altitude'),
            last_updated=response.get('last_updated')
        )
