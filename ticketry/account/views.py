from django.contrib.auth.models import User
from rest_framework.views import APIView
from serializers import BaseUserSerializer
from rest_framework.response import Response
from rest_framework.status import *

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