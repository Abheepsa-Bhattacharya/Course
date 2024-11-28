# projects/models.py

from django.db import models

class Topic(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.CharField(max_length=20) 
    image = models.FileField(upload_to="topic_images/", blank=True)
    