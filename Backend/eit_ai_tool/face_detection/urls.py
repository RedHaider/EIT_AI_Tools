from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from .views import face_detection , FaceDetectionListCreate, FaceDetectionListTable


urlpatterns = [
    path('', face_detection, name='face_detection'),
    path(
        'api/face_detection/',
          FaceDetectionListCreate.as_view(),
          name='face_detection_api'
          ),
    path(
        'api/face_detection_table/',
          FaceDetectionListTable.as_view(),
          name='face_detection_table_api'
          )
]