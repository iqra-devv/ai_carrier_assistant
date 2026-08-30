from django.urls import path
from .views import ResumeUploadView,ResumeAnalysisCreateView,ResumeSKillCreateView

urlpatterns = [
    path("upload/", ResumeUploadView.as_view(),name = "resume-upload"),
    path("<int:resume_id>/analyze/",ResumeAnalysisCreateView.as_view(),name='resume-analysis-create'),
    path("<int:resume_id>/skills/",ResumeSKillCreateView.as_view(),name="resume-skill-create"),
]