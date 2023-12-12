from django.db import models
from django.conf import settings
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
from destinations.models import Destination


# Create your models here.
class Attraction(models.Model):
    location = models.ForeignKey(
        Destination,
        on_delete=models.CASCADE,
    )
    name = models.CharField(primary_key=True, max_length=255)
    description = models.TextField(blank=False)
    address = models.TextField()
    rating = models.IntegerField(
        blank=False, validators=[MaxValueValidator(5), MinValueValidator(1)]
    )
    tags = models.TextField()
    numberReviews = models.IntegerField(default=1)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    image = models.ImageField(
        default="staticfiles/img/dest/no_image.jpg", upload_to="static/img/attr/"
    )

    def __str__(self):
        return self.name

    def get_url(self):
        return self.location.get_absolute_url()

    def get_absolute_url(self):
        return reverse("attraction_detail", kwargs={"pk": self.pk})


class AttractionComment(models.Model):
    attraction = models.ForeignKey(Attraction, on_delete=models.CASCADE)
    comment = models.CharField(max_length=255)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse("attraction_list")
