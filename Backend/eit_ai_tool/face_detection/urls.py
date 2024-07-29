from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from .views import face_detection


urlpatterns = [
    path('', face_detection, name='face_detection'),# root of face_detection app
]