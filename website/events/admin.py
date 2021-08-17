from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Guntur,EG
from import_export.admin import ImportExportModelAdmin
# Register your models here.
@admin.register(Guntur)
class excelSheet(ImportExportModelAdmin):
    pass
@admin.register(EG)
class excelSheet(ImportExportModelAdmin):
    pass