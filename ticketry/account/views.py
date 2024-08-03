from django.contrib.auth.models import User
from rest_framework.views import APIView
from .serializers import BaseUserSerializer, Userinfoserializer
from rest_framework.response import Response
from rest_framework.status import *
from .models import UserInfo

class UserView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            users = User.objects.all()
            serializer = BaseUserSerializer(users, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)}, status=HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request, *args, **kwargs):
        try:
            serializer = BaseUserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=HTTP_201_CREATED)
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=HTTP_500_INTERNAL_SERVER_ERROR)
        

class CreateUserInfoView(APIView):
    def get(self, request):
        try:
            users = UserInfo.objects.all()
            serializer = Userinfoserializer(users, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)}, status=HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            serializer = Userinfoserializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=HTTP_201_CREATED)
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=HTTP_500_INTERNAL_SERVER_ERROR)
        
class UpdateUserInfoView(APIView):
    def put(self, request, pk):
        try:
            user = UserInfo.objects.get(userid = pk)
            serializer = Userinfoserializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=HTTP_202_ACCEPTED)
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        except UserInfo.DoesNotExist as e:
            return Response({'error': str(e)}, status= HTTP_500_INTERNAL_SERVER_ERROR)

    def patch(self, request, pk):
        try:
            user = UserInfo.objects.get(userid = pk)
            serializer = Userinfoserializer(user, request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status= HTTP_202_ACCEPTED)
            return Response(serializer.errors, status= HTTP_400_BAD_REQUEST)
        except UserInfo.DoesNotExist as e:
            return Response({'error':str(e)}, status= HTTP_404_NOT_FOUND)
