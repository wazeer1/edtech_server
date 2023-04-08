from django.contrib import admin
from .models import *

# Register your models here.
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('pk', 'date_added','name', 'days')
    ordering = ('-date_added',)
    search_fields = ('pk', 'name')
    
admin.site.register(Program,ProgramAdmin)

class UserProgramAdmin(admin.ModelAdmin):
    list_display = ('pk', 'date_added')
    ordering = ('-date_added',)
    search_fields = ('pk',)
    
admin.site.register(UserProgram,UserProgramAdmin)


class CourseAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)
    ordering = ('order_id',)
    search_fields = ('pk',)
    
admin.site.register(Courses,CourseAdmin)


class ProfileCourseAdmin(admin.ModelAdmin):
    list_display = ('pk',)
    ordering = ('-date_added',)
    search_fields = ('pk',)
    
admin.site.register(ProfileCourses,ProfileCourseAdmin)


class LessonAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)
    ordering = ('-order_id',)
    search_fields = ('pk',)
    
admin.site.register(Lessons,LessonAdmin)


class LessonUserAdmin(admin.ModelAdmin):
    list_display = ('pk',)
    ordering = ('-date_added',)
    search_fields = ('pk',)
    
admin.site.register(ProfileLesson,LessonUserAdmin)