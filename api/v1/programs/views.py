from rest_framework import status
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from .serializers import *
from api.v1.main.functions import generate_serializer_errors
from programs.models import *
from django.contrib.auth.models import Group, User
from main.encryption import *
from datetime import timedelta
from main.functions import *
import requests
import json


@api_view(["GET"])
@permission_classes((AllowAny,))
def programs(request):
    instances = Program.objects.filter(is_deleted=False)
    serialized = ProgramSerializer(
        instances,
        context ={
        "request":request
        },
        many = True
    ).data
    response_data = {
        "StatusCode":6000,
        "data":serialized
    }
    return Response(response_data, status=status.HTTP_200_OK)


@api_view(["GET"])
def courses(request):
    if Courses.objects.filter(is_deleted=False).exists():
        instances = Courses.objects.filter(is_deleted=False)
        serialized = CoursesSerializer(
            instances,
            context = {
            "request":request
            },
            many = True
        ).data
        response_data ={
            "StatusCode":6000,
            "data":serialized
        }
    else:
        response_data = {
            "StatusCode":6001,
            "data":{
                "title":"failed",
                "message":"no courses found"
            }
        }
    return Response(response_data, status=status.HTTP_200_OK)



@api_view(["GET"])
def start_course(request,pk):
    if Courses.objects.filter(pk = pk, is_deleted=False).exists():
        course = Courses.objects.get(pk = pk, is_deleted=False)
        profile = Profiles.objects.get(user = request.user,is_deleted = False)
        lesson = Lessons.objects.filter(course = course, is_deleted=False).latest('order_id')
        profile_course = ProfileCourses.objects.create(
            profile = profile,
            course = course,
            auto_id = get_auto_id(ProfileCourses)
        )
        profile_lesson = ProfileLesson.objects.create(
            profile = profile,
            lesson = lesson,
            auto_id = get_auto_id(ProfileLesson)
        )
        response_data = {
            "StatusCode":6000
        }
    else:
        response_data={
            "StatusCode":6001,
            "data":{
            "title":"failed",
            "message":"campus not found"
            }
        }
    return Response(response_data, status=status.HTTP_200_OK)