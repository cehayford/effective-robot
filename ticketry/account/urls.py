from django.urls import path, include
from oauth2_provider import urls as oauth2_urls

urlpatterns = [
    path('oauth/', include(oauth2_urls)),
    path('auth/', include('djoser.urls')),
    # path('', ),
]