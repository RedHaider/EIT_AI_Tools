from rest_framework import serializers
from .models import FaceDetectionRecord

class FaceDetectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FaceDetectionRecord
        fields = ['id','name','timestamp']

class FaceDetectionSerializerTable(serializers.ModelSerializer):
    class Meta:
        model = FaceDetectionRecord
        fields = ['name','timestamp']