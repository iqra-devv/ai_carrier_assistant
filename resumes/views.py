from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .serializers import ResumeSerializer
# Create your views here.

class ResumeUploadView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request):
        serializer = ResumeSerializer(data = request.data)
        if serializer.is_valid():
            resume = serializer.save(user = request.user)

            return Response(
                ResumeSerializer(resume).data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
        
