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
from datetime import timedelta
import requests
import json
from programs.models import *

from main.functions import get_auto_id

@api_view(["POST"])
@permission_classes((AllowAny,))
def register_user(request):
    serialized = RegisterSerializers(data=request.data)
    if serialized.is_valid():
        name = request.data["name"]
        email = request.data["email"]
        password = request.data["password"]
        plan = request.data["plan"]
        try:
            photo = request.FILE["photo"]
        except:
            photo = None

        if not Profiles.objects.filter(username = email, is_deleted=False).exists():
            encrypted_password = encrypt(password)
            user = User.objects.create_user(
                username = email,
                password=password
            )
            plan = Program.objects.get(pk=plan, is_deleted=False)
            
            profile = Profiles.objects.create(
                name = name,
                email = email,
                user = user,
                username = email,
                password = encrypted_password,
                photo = photo,
                auto_id = get_auto_id(Profiles)
            )
            user_plan = UserProgram.objects.create(
                auto_id = get_auto_id(UserProgram),
                profile = profile,
                program = plan
            )
            headers = {
                "Content-Type" : "application/json"
            }

            data = {
                "username" : email,
                "password" : password,
            }
            points = ProfileCoins.objects.create(
                profile = profile,
                auto_id = get_auto_id(Profiles)
            )
            protocol = "http://"
            if request.is_secure():
                protocol = "https://"

            host = request.get_host()

            url = protocol + host + "/api/v1/accounts/token/"
            
            response = requests.post(url, headers=headers, data=json.dumps(data))

            if response.status_code == 200:

                response_data = {
                    "StatusCode":6000,
                    "data":{
                    "access":response.json()
                    }
                }
            else:
                response_data = {
                    "StatusCode":6001,
                    "data":{
                    "title":"failed",
                    "message":"something went wrong"
                    }
                }
        else:
            response_data={
                "StatusCode":6001,
                "data":{
                    "title":"failed",
                    "message":"email already exists"
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


@api_view(["POST"])
@permission_classes((AllowAny,))
def login_user(request):
    seriaized = LoginSerializers(data=request.data)
    if seriaized.is_valid():
        username = request.data["email"]
        password = request.data["password"]
        if Profiles.objects.filter(username = username, is_deleted=False).exists():
            profile = Profiles.objects.get(username = username, is_deleted=False)
            de_pass = decrypt(profile.password)
            if password == de_pass:
                headers = {
                "Content-Type" : "application/json"
                }

                data = {
                    "username" : username,
                    "password" : password,
                }
                protocol = "http://"
                if request.is_secure():
                    protocol = "https://"

                host = request.get_host()

                url = protocol + host + "/api/v1/accounts/token/"
                
                response = requests.post(url, headers=headers, data=json.dumps(data))
                response_data={
                    "StatusCode":6000,
                    "data":{
                    "access":response.json()
                    },
                }
            else:
                response_data={
                    "StatusCode":6001,
                    "data":{
                    "title":"failed",
                    "message":"password incorrect"
                    }
                }
        else:
            response_data={
                "StatusCode":6001,
                "data":{
                "title":"failed",
                "message":"this email do not have account"
                }
            }
    else:
        response_data = {
            "StatusCode": 6001,
            "data" : {
                "title": "Validation Error",
                "message": generate_serializer_errors(seriaized._errors)
            },
        }
    return Response(response_data, status=status.HTTP_200_OK)


@api_view(["GET"])
def minimal(request):
    user = request.user
    if Profiles.objects.filter(user = request.user, is_deleted=False).exists():
        profile = Profiles.objects.get(user = user, is_deleted=False)
        if profile.photo:
            photo = photo
        else:
            photo = None
        try:
            points = ProfileCoins.objects.get(profile = profile, is_deleted=False)
            points = points.points
        except:
            points = ''
        try:
            program = UserProgram.objects.filter(profile=profile, is_deleted=False).latest('date_added')
            days = program.program.days
            print(days,"days-=--=-=-=--=")
            end_date = profile.date_added
            end_date = profile.date_added + timedelta(days=days)
            end_date = end_date.strftime('%d/%m/%Y')
        except:
            end_date = ''
        response_data={
            "StatusCode":6000,
            "data":{
            "name":profile.name,
            "photo":photo,
            "points":points,
            "end_date":end_date
            }
        }
    else:
        response_data={
            "StatusCode":6001,
            "data":{
            "title":"failed",
            "message":"no user found"
            }
        }
    return Response(response_data, status=status.HTTP_200_OK)