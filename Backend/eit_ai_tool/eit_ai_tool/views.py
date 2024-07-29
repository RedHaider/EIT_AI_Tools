from django.contrib import admin
from django.urls import path
from django.shortcuts import render

# Define the view function
def home(request):
    return render(request, 'dashboard.html')