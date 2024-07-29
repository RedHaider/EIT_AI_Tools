from django import forms
from .models import NumberPlateDetection

class NumberPlateDetectionForm(forms.ModelForm):
    class Meta:
        model = NumberPlateDetection
        fields = ['number_plate_image', 'car_image']
