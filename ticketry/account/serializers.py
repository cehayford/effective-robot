from djoser.serializers import UserSerializer as BaseUserSerializer
from rest_framework import serializers
from .models import UserInfo, BookingHistory
from uuid import uuid4

class Userserializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = "['id', 'first_name', 'last_name', 'email']"


class Userinfoserializer(serializers.ModelSerializer):
    userid = serializers.UUIDField(read_only = True)
    class Meta:
        model = UserInfo
        fields = '__all__'

class Bookinghistoryserializer(serializers.ModelSerializer):
    historyid = serializers.UUIDField(read_only = True)
    class Meta:
        model = BookingHistory
        fields = '__all__'
        