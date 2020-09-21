from django.contrib import admin

from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin

from Data_App.models import DataFile

# Register your models here.

admin.site.register(DataFile, DraggableMPTTAdmin)
