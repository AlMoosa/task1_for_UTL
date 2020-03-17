from django.db import models


class Taskapp(models.Model):
    TASK_STATUS = {
        (1, 'В процессе'),
        (2, "В ожидании"),
        (3, "Законченный"),
    }
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    status = models.IntegerField(choices=TASK_STATUS, verbose_name='Status', default=2)
    created_at = models.DateTimeField(auto_now_add=True)
    finished_date = models.DateTimeField(auto_now=True, verbose_name="Дата завершения")
    tags = models.ManyToManyField("Tagapp", related_name='tasks', blank=True)

    def __str__(self):
        return self.title


class Tagapp(models.Model):
    title = models.CharField(max_length=120)
    date = models.DateField(auto_now=True, verbose_name='Дата тега')

    def __str__(self):
        return self.title
