from django.shortcuts import render, redirect
# from .models import FaceDetectionRecord
from django.http import HttpResponse
from .models import FaceDetectionRecord
from .forms import FaceDetectionRecordForm
from rest_framework import generics
from .serializers import FaceDetectionSerializer, FaceDetectionSerializerTable



def face_detection(request):
    if request.method == "POST":
        form = FaceDetectionRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('face_detection')
    else:
        form = FaceDetectionRecordForm()
    
    data = FaceDetectionRecord.objects.all()
    return render(request, 'face_detection.html', {'data': data, 'form': form})

class FaceDetectionListCreate(generics.ListCreateAPIView):
    queryset = FaceDetectionRecord.objects.all()
    serializer_class = FaceDetectionSerializer

class FaceDetectionListTable(generics.ListCreateAPIView):
    queryset = FaceDetectionRecord.objects.all()
    serializer_class = FaceDetectionSerializerTable
