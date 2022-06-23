from django.contrib import admin

from web.models import Industry


class IndustryAdmin(admin.ModelAdmin):
    list_display = ['id','auto_id','date_added','date_updated','is_deleted','name','image']
    readonly_fields= ['date_added','date_updated']

admin.site.register(Industry, IndustryAdmin)
