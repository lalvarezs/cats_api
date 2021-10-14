from django.http import response
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import APIView
from accounts.models import User
from accounts.api.serializers import UserRegisterSerializer


class UserRegisterView(APIView):
    serializer = UserRegisterSerializer()

    def post(self, request, format=None):
        response,status = self.serializer.validate_fields(request)
        if status != 200:
            return Response(response,status)
        
        response, status = self.serializer.create_user(request)
        return Response(response,status)