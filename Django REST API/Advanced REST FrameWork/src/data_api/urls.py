from django.contrib import admin
from django.urls import path, include
from core.views import PostView, PostCreateView, PostListCreateView
from rest_framework.authtoken.views import obtain_auth_token # will return the token to a user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PostView.as_view(), name='post'),
    path('create/', PostCreateView.as_view(), name='post'),
    path('list-create/', PostListCreateView.as_view(), name='post'),
    path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('api/token/', obtain_auth_token, name='obtain-token')
]
