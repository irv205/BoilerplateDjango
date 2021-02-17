from django.urls import path, re_path
from rest_framework import routers
from django.shortcuts import render
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView
)
from . import views

router = routers.DefaultRouter()

router.register('user', views.UserView, basename='get_user')

urlpatterns = [
    path('login/', views.getauthenticationtokenRefresh.as_view(), name='get_access_token'),
    path('refresh-token/', TokenRefreshView.as_view(), name='get_new_access_token'),
    path('register/', views.RegisterUserView.as_view(), name='register_user'),
    re_path(r'^update-user/(?P<pk>[0-9]+)/$', views.UpdateUserView.as_view()),
]

urlpatterns += router.urls