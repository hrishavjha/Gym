from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=120, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    des = models.CharField(max_length=500, blank=True, null=True)
    # img = models.ImageField(null=True, blank=True, des="services_img")
    is_enrolled = models.BooleanField(null=True, blank=True, default=False)

    def __str__(self):
        return str(self.name)
