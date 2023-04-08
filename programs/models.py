from django.db import models
from main.models import BaseModel
import uuid
from versatileimagefield.fields import VersatileImageField


# Create your models here.
class Program(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, blank=True, null=True)
    days = models.PositiveBigIntegerField(default=30, blank=True, null=True)
    

    class Meta:
        db_table = 'programs_program'
        verbose_name = 'program'
        verbose_name_plural = 'programs'
        ordering = ('date_added',)


    def __str__(self):
        return self.name
    

class UserProgram(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    profile = models.ForeignKey('accounts.Profiles', on_delete = models.CASCADE)
    program = models.ForeignKey('programs.Program', on_delete=models.CASCADE)

    class Meta:
        db_table = 'programs_user_program'
        verbose_name = 'user_program'
        verbose_name_plural = 'user_programs'
        ordering = ('date_added',)

    def __str__(self):
        return self.program.name
    

class Courses(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order_id = models.PositiveBigIntegerField(default=0,blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    course_time = models.TimeField(blank=True, null=True)
    image = VersatileImageField(upload_to="static/courses/",blank=True,null=True)

    class Meta:
        db_table = 'programs_courses'
        verbose_name = 'course'
        verbose_name_plural = 'courses'
        ordering = ('date_added',)

    def __str__(self):
        return self.name
    

class Lessons(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order_id = models.PositiveBigIntegerField(default=0,blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    duration = models.DurationField()
    course = models.ForeignKey('programs.Courses', on_delete=models.CASCADE)
    image = VersatileImageField(upload_to="static/lessons_cover/",blank=True,null=True)
    video = models.FileField(upload_to='static/lessons/', blank=True, null=True)

    class Meta:
        db_table = 'programs_lessons'
        verbose_name = 'lesson'
        verbose_name_plural = 'lessons'
        ordering = ('date_added',)

    def __str__(self):
        return self.name



class ProfileCourses(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    course = models.ForeignKey('programs.Courses', on_delete=models.CASCADE)
    profile = models.ForeignKey('accounts.Profiles', on_delete=models.CASCADE)
    is_activated = models.BooleanField(default=False, blank=True, null=True)

    class Meta:
        db_table = 'programs_profile_course'
        verbose_name = 'profile course'
        verbose_name_plural = 'profile courses'
        ordering = ('date_added',)

    def __str__(self):
        return self.course.name
    

class ProfileLesson(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    lesson = models.ForeignKey('programs.Lessons', on_delete=models.CASCADE)
    profile = models.ForeignKey('accounts.Profiles', on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False, blank=True, null=True)

    class Meta:
        db_table = 'programs_profile_lessons'
        verbose_name = 'profile lesson'
        verbose_name_plural = 'profile lessons'
        ordering = ('date_added',)

    def __str__(self):
        return self.course.name
    

    