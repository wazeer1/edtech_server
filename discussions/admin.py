from django.contrib import admin
from .models import *

# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('pk','question')
    ordering = ('-date_added',)
    search_fields = ('pk','question')
    
admin.site.register(Question,QuestionAdmin)

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('pk','answer')
    ordering = ('-date_added',)
    search_fields = ('pk','answer')
    
admin.site.register(Answer,AnswerAdmin)