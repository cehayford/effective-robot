from django.urls import path, include
from oauth2_provider import urls as oauth2_urls
from .views import signup
urlpatterns = [
    path('oauth/', include(oauth2_urls)),
    # path('auth/', include('knox.urls')),
    # path('auth/signup', signup),
    # path('', ),
]