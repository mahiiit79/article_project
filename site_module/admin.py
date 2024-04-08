from django.contrib import admin
from . import models
# Register your models here.



class SiteBannerAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'position']



admin.site.register(models.SiteBanner, SiteBannerAdmin)
admin.site.register(models.SiteSetting)