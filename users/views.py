from flask import Response
from itsdangerous import Serializer
from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from rest_framework.response import Response
# Create your views here.
class RegisterApi(CreateAPIView):
    queryset = User.objects.all();
    serializer_class = RegisterSerializer
    
    #*overwrite post to give response message, token can be added either
    def post(self, request, *args, **kwargs):
        #*data in serializer
        serializer = RegisterSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message':'user created succesfully'})