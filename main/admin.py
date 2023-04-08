from django.contrib import admin

from main.models import  Mode



class ModeAdmin(admin.ModelAdmin):
    list_display = ('down', 'maintenance', 'readonly')

admin.site.register(Mode,ModeAdmin)
