from django.urls import path, include
from cats.api.viewsets import CatList
from rest_framework.authtoken import views

urlpatterns = [
    path('cats/', CatList.as_view())
]