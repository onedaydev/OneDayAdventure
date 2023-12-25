from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from adventure.adventure_options import CLASS_CHOICES, RACE_CHOICES


class Adventure(models.Model):
    user = models.ForeignKey(
        "users.User",
        verbose_name="adventurer",
        on_delete=models.CASCADE,
    )
    character_age = models.IntegerField(
        verbose_name="캐릭터 나이", validators=[MinValueValidator(12), MaxValueValidator(60)]
    )
    character_class = models.CharField(verbose_name="캐릭터 직업", choices=CLASS_CHOICES)
    character_race = models.CharField(verbose_name="캐릭터 종족", choices=RACE_CHOICES)

    status = models.CharField(blank=True)
    date = models.DateTimeField(verbose_name="create date", auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Adventure(id: {self.id}"


class Report(models.Model):
    user = models.ForeignKey(
        "users.User",
        verbose_name="adventurer",
        on_delete=models.CASCADE,
    )
    adventure = models.ForeignKey(
        Adventure,
        verbose_name="adventure",
        on_delete=models.CASCADE,
    )
    report_content = models.TextField(verbose_name="Report Content")
    date = models.DateTimeField(verbose_name="create date", auto_now_add=True)

    def __str__(self):
        return f"Report by {self.user.username} for Adventure {self.adventure.id}"
