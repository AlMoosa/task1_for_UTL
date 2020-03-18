# Generated by Django 2.2 on 2020-03-17 14:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tagapp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Название тега')),
                ('date', models.DateField(auto_now=True, verbose_name='Дата тега')),
                ('author', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор тега')),
            ],
        ),
        migrations.CreateModel(
            name='Taskapp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Название')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('status', models.IntegerField(choices=[(1, 'В процессе'), (2, 'В ожидании'), (3, 'Законченный')], default=2, verbose_name='Статус')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('finished_date', models.DateTimeField(auto_now=True, verbose_name='Дата завершения')),
                ('author', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('tags', models.ManyToManyField(blank=True, related_name='tasks', to='taskapp.Tagapp')),
            ],
        ),
    ]
