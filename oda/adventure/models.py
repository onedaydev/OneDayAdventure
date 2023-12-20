from django.db import models


class Adventure(models.Model):
    user = models.ForeignKey(
        "users.User",
        verbose_name="adventurer",
        on_delete=models.CASCADE,
    )
    parameters1 = models.TextField("변수1")
    parameters2 = models.TextField("변수2")
    parameters3 = models.TextField("변수3")
    date = models.DateTimeField(auto_now_add=True)

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
        on_delete=models.CASCADE,
    )
    report_content = models.TextField("Report Content")
    etc = models.TextField("Etc")
    date = models.DateTimeField(auto_now_add=True)
