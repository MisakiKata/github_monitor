from django.contrib import admin
from .models import Warename
# Register your models here.

@admin.register(Warename)
class WarenameAdmin(admin.ModelAdmin):
    list_display = ('name', 'dealwith')