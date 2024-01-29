from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

User = get_user_model()


class Package(models.Model):
    user = models.ForeignKey(
        User, verbose_name="Пользователь", on_delete=models.CASCADE
    )
    cam_id = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(99)]
    )
    video_color = models.JSONField()
    time_section = models.DateTimeField(auto_now_add=True)
    channel_no = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(2)]
    )
    config_no = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(1)]
    )
