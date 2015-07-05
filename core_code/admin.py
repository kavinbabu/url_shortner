from django.contrib import admin
from core_code.models import DataMaster

# Register your models here.
class DataMasterAdmin(admin.ModelAdmin):
    list_display = ('id', 'url_string', 'md5_hash')
    list_filter = ('id', 'url_string', 'md5_hash')
    list_display_links = ('url_string',)


admin.site.register(DataMaster, DataMasterAdmin)
