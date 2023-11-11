from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    country = models.CharField(max_length = 30, null=False, blank=False)

    class StatusRank(models.TextChoices):
        Egg = "Egg"
        Hatchling = "Hatchling"
        Nestling = "Nestling"
        Fledgeling = "Fledgeling"
        Flapping = "Flapping"
        Flying = "Flying"
        Soaring = "Soaring"
        
    status = models.CharField(
        max_length = 10,
        choices = StatusRank.choices,
        default = StatusRank.Egg,
        null = False,
    )

    numContributions = models.IntegerField(default = 0, null=False)

    
