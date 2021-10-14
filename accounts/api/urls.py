from django.urls import path, include
from accounts.api.viewsets import UserRegisterView
from rest_framework.authtoken import views

urlpatterns = [
    path('register/', UserRegisterView.as_view()),
    path('token/', views.obtain_auth_token)
]