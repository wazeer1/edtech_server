from rest_framework import serializers


class RegisterSerializers(serializers.Serializer):
    name = serializers.CharField()
    password = serializers.CharField()
    email = serializers.CharField()
    plan = serializers.CharField()

class LoginSerializers(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()
