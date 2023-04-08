from django.contrib import admin
from .models import *

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('pk', 'date_added','name', 'email','password')
    ordering = ('-date_added',)
    search_fields = ('pk', 'name')
    
admin.site.register(Profiles,ProfileAdmin)


class ProfileCoinAdmin(admin.ModelAdmin):
    list_display = ('pk', 'points')
    ordering = ('-date_added',)
    search_fields = ('pk',)
    
admin.site.register(ProfileCoins,ProfileCoinAdmin)