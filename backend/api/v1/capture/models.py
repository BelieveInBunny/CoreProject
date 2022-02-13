from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class CaptureModel(models.Model):
    user = models.ForeignKey(
        get_user_model(), related_name="user", on_delete=models.CASCADE
    )
    video_volume = models.IntegerField(
        default=50,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0),
        ],
    )
