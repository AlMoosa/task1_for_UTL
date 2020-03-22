from django.contrib import admin
from .models import Taskapp, Tagapp



class TaskAppAdmin(admin.ModelAdmin):
    # pass
    # model = Taskapp
    list_display = ['title', 'author', 'description', 'status', 'created_at', 'finished_date']
# 


class TagappAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'date']

admin.site.register(Taskapp, TaskAppAdmin)
admin.site.register(Tagapp, TagappAdmin)