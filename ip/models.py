from django.db import models


# Create your models here.
class ip(models.Model):
    ipAddress = models.CharField("ip address", max_length=255, blank=True, null=True)
    root = models.CharField("Root Username", max_length=255, blank=True, null=True)
    password = models.CharField("Root Password", max_length=255, blank=True, null=True)
    additionalUser = models.CharField("Additional user", max_length=255, blank=True, null=True)
    additionalPassword = models.CharField("Additional User's password", max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    createdAt = models.DateTimeField("Created At", auto_now_add=True)

    def __str__(self):
        return self.ipAddress
