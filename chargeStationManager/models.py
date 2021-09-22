from django.db import models
from django.contrib.auth import get_user_model


class ChargePoint(models.Model):
    id = models.AutoField(primary_key=True)
    station_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    point_number = models.CharField(max_length=50)
    occupied = models.BooleanField(default=False)

    def __str__(self):
        return self.station_id.station_name