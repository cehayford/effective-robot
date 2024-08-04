from django.contrib.auth.models import User
from rest_framework.views import APIView
from .serializers import BaseUserSerializer, Userinfoserializer, Bookinghistoryserializer
from rest_framework.response import Response
from rest_framework.status import *
from .models import UserInfo, BookingHistory
# from rest_framework.decorators import api_view

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
            history = BookingHistory.objects.all()
            user_serializer = Userinfoserializer(users, many=True),
            history_serializer = Bookinghistoryserializer(history, many=True)
            comeback = {
                'users': user_serializer,
                'history': history_serializer
            }
            return Response(comeback.data)
        except Exception as e:
            return Response({'error': str(e)}, status=HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            user_serializer = Userinfoserializer(data=request.data)
            history_serializer = Bookinghistoryserializer(data=request.data)
            if user_serializer.is_valid():
                user_serializer.save()
            else:
                return Response(user_serializer.errors, status=HTTP_400_BAD_REQUEST)

            if history_serializer.is_valid():
                history_serializer.save()
            else:
                return Response(history_serializer.errors, status=HTTP_400_BAD_REQUEST)
            comeback = {
                'users': user_serializer,
                'history': history_serializer
            }
            return Response(comeback.data, status=HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=HTTP_500_INTERNAL_SERVER_ERROR)


# @api_view(['PUT', 'PATCH'])
class UpdateUserInfoView(APIView):
    def put(self, request, pk):
        try:
            user = UserInfo.objects.get(userid = pk)
            history = BookingHistory.objecjs.get(historyid = pk)
            user_serializer = Userinfoserializer(user, data=request.data)
            history_serializer = Bookinghistoryserializer(history, data=request.data)
            if user_serializer.is_valid():
                user_serializer.save()
            else:
                return Response(user_serializer.errors, status=HTTP_400_BAD_REQUEST)

            if history_serializer.is_valid():
                history_serializer.save()
            else:
                return Response(history_serializer.errors, status=HTTP_400_BAD_REQUEST)
            comeback = {
                'user' : user_serializer,
                'history' : history_serializer
            }
            return Response(comeback.data, status=HTTP_202_ACCEPTED)
        except UserInfo.DoesNotExist as e:
            return Response({'error': str(e)}, status= HTTP_500_INTERNAL_SERVER_ERROR)

    def patch(self, request, pk):
        try:
            user = UserInfo.objects.get(userid = pk)
            history = BookingHistory.objecjs.get(historyid = pk)
            user_serializer = Userinfoserializer(user, data=request.data)
            history_serializer = Bookinghistoryserializer(history, data=request.data)
            if user_serializer.is_valid():
                user_serializer.save()
            else:
                return Response(user_serializer.errors, status=HTTP_400_BAD_REQUEST)

            if history_serializer.is_valid():
                history_serializer.save()
            else:
                return Response(history_serializer.errors, status=HTTP_400_BAD_REQUEST)
            comeback = {
                'user' : user_serializer,
                'history' : history_serializer
            }
            return Response(comeback.data, status=HTTP_202_ACCEPTED)
        except UserInfo.DoesNotExist as e:
            return Response({'error':str(e)}, status= HTTP_404_NOT_FOUND)
