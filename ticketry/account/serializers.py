from djoser.serializers import UserSerializer as BaseUserSerializer
from rest_framework import serializers
from .models import UserInfo
from uuid import uuid4

class Userserializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = "['id', 'first_name', 'last_name', 'email']"


class Userinfoserializer(serializers.ModelSerializer):
    userid = serializers.UUIDField(read_only = True)
    class Meta:
        models = UserInfo
        fields = '__all__'
        