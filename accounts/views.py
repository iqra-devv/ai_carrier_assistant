from django.shortcuts import render

from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import RegisterSerializer

# Creates a user registration API endpoint using Django REST Framework.
# It uses RegisterSerializer to validate the submitted registration data
# and create a new user, while AllowAny allows both authenticated and
# unauthenticated users to access this endpoint.

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

