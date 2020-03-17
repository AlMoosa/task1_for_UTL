from django.contrib import admin
from .models import Taskapp, Tagapp



class TaskAppAdmin(admin.ModelAdmin):
    # pass
    # model = Taskapp
    list_display = ['title', 'description', 'status', 'created_at', 'finished_date']


class TagappAdmin(admin.ModelAdmin):
    list_display = ['title', 'date']

admin.site.register(Taskapp, TaskAppAdmin)
admin.site.register(Tagapp, TagappAdmin)