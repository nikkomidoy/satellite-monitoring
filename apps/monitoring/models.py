from django.db import models
from django.utils.timezone import localtime


class SatelliteData(models.Model):
    """
    Satellite data model
    """
    altitude = models.DecimalField(
        max_digits=30,
        decimal_places=15,
        help_text="Satellite's altitude in kilometers"
    )
    last_updated = models.DateTimeField(help_text="Last recorded date from the satellite's data in UTC")
    created_at = models.DateTimeField(default=localtime)

    class Meta:
        verbose_name_plural = "Satellite datum"

    def __str__(self):
        return f"Altitude - {self.altitude}"
