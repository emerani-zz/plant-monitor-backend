from django.db import models

# Create your models here.


class PlantStatus(models.Model):
    status_time = models.DateTimeField(auto_now_add=True)
    humidity = models.CharField(max_length=10, blank=True)
    temperature = models.CharField(max_length=10, blank=True)
    light_exposure = models.CharField(max_length=10, blank=True)
    uv_level = models.CharField(max_length=10, blank=True)
    soil_moisture = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return "{}".format(self.status_time)
