from rest_framework import serializers
from .models import NumberPlateDetection

class NumberPlateDetectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = NumberPlateDetection
        fields = ['id', 'timestamp', 'number_plate_image', 'car_image']

class NumberPlateDetectionSerializerTable(serializers.ModelSerializer):
    class Meta:
        model = NumberPlateDetection
        fields= ['timestamp', 'number_plate_image','car_image']