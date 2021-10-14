from django.http import response
from rest_framework.response import Response
from rest_framework.decorators import APIView
from accounts.models import User
from rest_framework.permissions import IsAuthenticated
from cats.api.serializers import CatSerializer

class CatList(APIView):
    permission_classes = [IsAuthenticated]
    serializer = CatSerializer()
    
    def get(self, request): 
        pass

    def post(self, request, format=None):
        response,status = self.serializer.validate_fields(request)
        if status != 200:
            return Response(response,status)
        
        response, status = self.serializer.create_cat(request)
        return Response(response,status)

