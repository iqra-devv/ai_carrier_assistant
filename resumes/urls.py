from django.urls import path
from .views import ResumeUploadView,ResumeAnalysisCreateView

urlpatterns = [
    path("upload/", ResumeUploadView.as_view(),name = "resume-upload"),
    path("<int:resume_id>/analyze",ResumeAnalysisCreateView.as_view(),name='resume-analysis-create'),
]