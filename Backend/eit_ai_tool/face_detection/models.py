from django.db import models

class FaceDetectionRecord(models.Model):
    name = models.CharField(max_lenght=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    
