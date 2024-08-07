from django.shortcuts import render, redirect
from .models import NumberPlateDetection
from .forms import NumberPlateDetectionForm
from .serializers import NumberPlateDetectionSerializer, NumberPlateDetectionSerializerTable
from rest_framework import generics

def number_plate_detection(request):
    if request.method == 'POST':
        form = NumberPlateDetectionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('number_plate_detection')
    else:
        form = NumberPlateDetectionForm()
    
    data = NumberPlateDetection.objects.all()
    return render(
        request, 'numberplate_detection.html',
        {
            'data': data,
            'form': form
        }
    )

class NumberPlateDetectionListCreate(generics.ListCreateAPIView):
    queryset = NumberPlateDetection.objects.all()
    serializer_class = NumberPlateDetectionSerializer


class NumberPlateDetectionListTable(generics.ListCreateAPIView):
    queryset = NumberPlateDetection.objects.all()
    serializer_class = NumberPlateDetectionSerializerTable