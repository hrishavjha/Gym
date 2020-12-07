from django.contrib.auth.models import User
from django.db import models


class ExtendedUser(models.Model):
    user = models.ForeignKey(
        User, null=True,
        on_delete=models.CASCADE,
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ph_no = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = "Extended Details"

    def __str__(self):
        return str(self.name)
