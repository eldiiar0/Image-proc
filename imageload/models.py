from django.db import models

class UploadedImage(models.Model):
    image = models.ImageField(upload_to='media/')
    uploaded_at = models.DateTimeField(auto_now_add=True)