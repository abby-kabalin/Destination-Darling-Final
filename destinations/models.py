from django.conf import settings
from django.db import models
from django.urls import reverse


class Destination(models.Model):
    location = models.CharField(max_length=255, primary_key=True)
    details = models.TextField()
    country = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.location

    def get_absolute_url(self):
        return reverse("destination_detail", kwargs={"pk": self.pk})


class Destination_Comment(models.Model):
    location = models.ForeignKey(Destination, on_delete=models.CASCADE)
    comment = models.CharField(max_length=255, primary_key=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse("destination_list")
