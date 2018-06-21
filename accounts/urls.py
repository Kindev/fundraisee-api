from django.urls import path

from .views import (
    UserCreateAPIView,
    UserLoginAPIView,
    UserLogoutAPIView,
    UserDetailAPIView,
    UserListAPIView,
    UserUpdateAPIView
)

urlpatterns = [
    path('', UserListAPIView.as_view(), name='user-list'),
    path('register/', UserCreateAPIView.as_view(), name='user-register'),
    path('login/', UserLoginAPIView.as_view(), name='user-login'),
    path('logout/', UserLogoutAPIView.as_view(), name='user-logout'),
    path('<slug:username>/', UserDetailAPIView.as_view(), name='user-detail'),
    path('<slug:username>/edit/', UserUpdateAPIView.as_view(), name='user-update'),
]