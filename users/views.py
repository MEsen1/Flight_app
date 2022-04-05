from itsdangerous import Serializer
from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import User
from .serializers import RegisterSerializer
# Create your views here.
class RegisterApi(CreateAPIView):
    queryset = User.objects.all();
    serializer_class = RegisterSerializer
    