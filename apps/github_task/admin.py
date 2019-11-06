from django.contrib import admin
from .models import edit_task
# Register your models here.


@admin.register(edit_task)
class editadmin(admin.ModelAdmin):
    list_display = ('task_name',)