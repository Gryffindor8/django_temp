from django.contrib import admin
from .models import *


# Register your models here.
class Adminfile(admin.ModelAdmin):
    list_display = ('tracking_id', 'file_name', 'created_at')


class Admintransaction(admin.ModelAdmin):
    list_display = ('file', 'assigned_to', 'created_at', 'is_active')


admin.site.register(files, Adminfile)
admin.site.register(transaction, Admintransaction)
