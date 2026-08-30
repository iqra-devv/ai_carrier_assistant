from rest_framework import serializers
from .models import Resume,ResumeAnalysis,Resume_SKill

class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields =[
            "id",
            "file",
            "uploaded_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "uploaded_at",
            "updated_at",
        ]

class ResumeAnalysisSerializer(serializers.ModelSerializer):
    resume = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = ResumeAnalysis
        fields = [
            "id",
            "resume",
            "extracted_text",
            "summary",
            "education",
            "experience",
            "projects",
            "certifications",
            "ats_score",
            "strengths",
            "weaknesses",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "extracted_text",
            "created_at",
            "updated_at",
        ]

class ResumeSkillSerializer(serializers.ModelSerializer):
    resume = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Resume_SKill
        fields = [
            "id",
            "resume",
            "skill",
        ] 
        read_only_fields = [
            "id"
            "resume"
        ]

