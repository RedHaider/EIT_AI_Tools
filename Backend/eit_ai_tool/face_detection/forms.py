from django import forms
from .models import FaceDetectionRecord

class FaceDetectionRecordForm(forms.ModelForm):
    class Meta:
        model = FaceDetectionRecord
        fields = ['name']
