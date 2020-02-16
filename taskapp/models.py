from django.db import models


class Taskapp(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField("Tagapp", related_name='tasks', blank=True)

    def __str__(self):
        return self.title


class Tagapp(models.Model):
    title = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
