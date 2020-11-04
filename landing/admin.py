from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Setting, Notify

# Register your models here.

admin.site.register(Setting)

@admin.register(Notify)
class NotifyAdmin(ImportExportModelAdmin):
    pass