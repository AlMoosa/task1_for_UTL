from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Taskapp(models.Model):
    TASK_STATUS = {
        (1, 'В процессе'),
        (2, "В ожидании"),
        (3, "Законченный"),
    }
    author = models.ForeignKey(
        User, blank=True, verbose_name='Автор', on_delete=models.CASCADE)
    title = models.CharField(max_length=120, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')
    status = models.IntegerField(
        choices=TASK_STATUS, verbose_name='Статус', default=2)
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата создания')
    finished_date = models.DateTimeField(
        auto_now=True, verbose_name="Дата завершения")
    tags = models.ManyToManyField("Tagapp", related_name='tasks', blank=True)

    def __str__(self):
        return self.title


class Tagapp(models.Model):
    author = models.ForeignKey(
        User, blank=True, verbose_name='Автор тега', on_delete=models.CASCADE)
    title = models.CharField(max_length=120, verbose_name='Название тега')
    date = models.DateField(auto_now=True, verbose_name='Дата тега')
    #   maybe here must be '''tasks = models.ManyToManyField("Tagapp", related_name='tasks', blank=True)'''

    def __str__(self):
        return self.title
