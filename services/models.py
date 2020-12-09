import os
from django.db import models


def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)


class Service(models.Model):
    name = models.CharField(max_length=120, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    des = models.CharField(max_length=500, blank=True, null=True)
    img = models.ImageField(null=True, blank=True, upload_to=get_image_path)
    is_enrolled = models.BooleanField(null=True, blank=True, default=False)

    def __str__(self):
        return str(self.name)
