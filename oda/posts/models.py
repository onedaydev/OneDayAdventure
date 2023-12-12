from django.db import models


class Post(models.Model):
    user = models.ForeignKey(
        "users.User",
        verbose_name="writer",
        on_delete=models.CASCADE,
    )
    title = models.TextField("title")
    content = models.TextField("Content")
    date = models.DateTimeField("create or modify date", auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Post(id: {self.id}, title: {self.title})"

class Comment(models.Model):
    user = models.ForeignKey(
        "users.User",
        verbose_name="writer",
        on_delete=models.CASCADE,
    )
    post = models.ForeignKey(
        Post,
        verbose_name="Post",
        on_delete=models.CASCADE,
    )
    content = models.TextField("Content")
    date = models.DateTimeField("create or modify date", auto_now_add=True)
