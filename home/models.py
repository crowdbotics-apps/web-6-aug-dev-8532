from django.conf import settings
from django.db import models

# Create your models here.

from django.db import models


class CustomText(models.Model):
    title = models.BinaryField(max_length=150, null=True, blank=True,)
    test12 = models.BigIntegerField(null=True, blank=True,)
    test54 = models.BigIntegerField(null=True, blank=True,)
    nameChangedAgain = models.CharField(null=True, blank=True, max_length=256,)

    def __str__(self):
        return self.title

    @property
    def api(self):
        return f"/api/v1/customtext/{self.id}/"

    @property
    def field(self):
        return "title"


class HomePage(models.Model):
    body212 = models.TextField(null=True, blank=True,)

    @property
    def api(self):
        return f"/api/v1/homepage/{self.id}/"

    @property
    def field(self):
        return "body"
