from rest_framework import serializers
from programs.models import *
from accounts.models import *

class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = (
            'id',
            'name'
        )

class CoursesSerializer(serializers.ModelSerializer):
    lessons = serializers.SerializerMethodField()
    is_started = serializers.SerializerMethodField()
    class Meta:
        model = Courses
        fields = (
            'id',
            'name',
            'lessons',
            'image',
            'lessons',
            'is_started'
        )
    
    def get_lessons(self,instance):
        lessons = Lessons.objects.filter(course = instance, is_deleted=False).count()
        return lessons
    
    def get_is_started(self,instance):
        request = self.context.get('request')
        profile = Profiles.objects.get(user=request.user,is_deleted=False)
        if ProfileCourses.objects.filter(course=instance, profile=profile, is_deleted=False).exists():
            is_started = True
        else:
            is_started = False
        return is_started