from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView
from .models import Resume
from .serializers import ResumeSerializer,ResumeAnalysisSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.exceptions import PermissionDenied
from .utils import extracted_text_from_pdf
# Create your views here.

class ResumeUploadView(CreateAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    parser_classes = [MultiPartParser, FormParser]

    permission_classes = [IsAuthenticated]

    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ResumeAnalysisCreateView(CreateAPIView):
    serializer_class = ResumeAnalysisSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        resume_id = self.kwargs["resume_id"]
        try:
            resume = Resume.objects.get(
                id = resume_id,
                user = self.request.user
            )
        except Resume.DoesNotExist:
            raise PermissionDenied(
                "You do not have permission to analyze this resume."
            )

        print(resume)
        extracted_text = extracted_text_from_pdf(resume.file)
        serializer.save(resume = resume, extracted_text = extracted_text,)

