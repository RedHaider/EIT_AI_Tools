from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from .views import number_plate_detection


urlpatterns = [
    path('',number_plate_detection , name='number_plate_detection'),# root of face_detection app
]