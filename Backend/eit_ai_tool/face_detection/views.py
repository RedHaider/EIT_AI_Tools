from django.shortcuts import render, redirect
# from .models import FaceDetectionRecord
from django.http import HttpResponse



# Create your views here.
def face_detection(request):
    # data = FaceDetectionRecord.objects.all()
    return render(request,'dashboard.html')