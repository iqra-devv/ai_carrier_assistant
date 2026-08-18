from django.db import models
from django.conf import settings

# Create your models here.
class Resume(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="resumes",
    )
    file = models.FileField(upload_to = "resumes/")
    uploaded_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.file.name}"

class ResumeAnalysis(models.Model):

    resume = models.OneToOneField(
        Resume,
        on_delete=models.CASCADE,
        related_name="analysis",
    )
    
    extracted_text = models.TextField(blank=True,null=True)
    summary = models.TextField(blank=True,null=True)
    experience = models.JSONField(default=list,blank=True)
    education = models.JSONField(default=list,blank=True)
    projects = models.JSONField(default=list,blank=True)
    certifications = models.JSONField(default=list, blank=True)
    ats_score = models.FloatField(null=True, blank=True)
    strengths = models.JSONField(default=list, blank=True)
    weaknesses = models.JSONField(default=list, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Analysis for Resume {self.resume.id}"
