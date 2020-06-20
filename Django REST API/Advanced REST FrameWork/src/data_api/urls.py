from django.contrib import admin
from django.urls import path, include
from core.views import TestView
from rest_framework.authtoken.views import obtain_auth_token # will return the token to a user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TestView.as_view(), name='test'),
    path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('api/token/', obtain_auth_token, name='obtain-token')
]
