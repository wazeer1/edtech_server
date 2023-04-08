from rest_framework import status
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from .serializers import *
from api.v1.main.functions import generate_serializer_errors
from accounts.models import *
from django.contrib.auth.models import Group, User
from main.encryption import *
from main.functions import *
from datetime import timedelta
import requests
import json
from discussions.models import *


@api_view(["GET"])
@permission_classes((AllowAny,))
def questions(request):
    if Question.objects.filter(is_deleted=False).exists():
        instances = Question.objects.filter(is_deleted=False)
        serialized = QuestionSerializer(
            instances,
            context = {
            "request":request
            },
            many = True
        ).data
        response_data = {
            "StatusCode":6000,
            "data":serialized
        }
    else:
        response_data={
            "StatusCode":6001,
            "data":{
            "title":"failed",
            "message":"no questions"
            }
        }
    return Response(response_data, status=status.HTTP_200_OK)


@api_view(["POST"])
def add_questions(request):
    serialized = AddQuestionSerializer(data=request.data)
    if serialized.is_valid():
        question = request.data["question"]
        topic = request.data["topic"]
        if not Question.objects.filter(question=question, is_deleted=False).exists():
            profile = Profiles.objects.get(user = request.user, is_deleted=False)
            question = Question.objects.create(
                user = profile,
                question = question,
                topic = topic,
                auto_id = get_auto_id(Question)
            )
            response_data={
                "StatusCode":6000,
                "data":{
                "title":"success",
                "message":"question submitted"
                }
            }
        else:
            response_data = {
                "StatusCode":6001,
                "data":{
                "title":"failed",
                "message":"question already exists"
                }
            }
    else:
        response_data = {
            "StatusCode": 6001,
            "data" : {
                "title": "Validation Error",
                "message": generate_serializer_errors(serialized._errors)
            },
        }
    return Response(response_data, status=status.HTTP_200_OK)