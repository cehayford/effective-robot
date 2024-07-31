# from rest_framework.status import *
# from rest_framework.response import Response
# from django.contrib.auth.models import User
# from rest_framework.authtoken.models import Token as Gem 
# from .serializers import Userserializer

# # Create your views here.
# def signup(request):
#     serializer = Userserializer(data = request.data)
#     serve = Userserializer.data
#     if serializer.is_valid():
#         user = serializer.save()
#         token, _ = Gem.objects.get_or_create(user = user)
#         return Response(
#             {
#                 'user': serve,
#                 'token': token.save
#             },
#             status= HTTP_201_CREATED
#         )
#     return Response(serializer.errors, status= HTTP_400_BAD_REQUEST)