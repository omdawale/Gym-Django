from django.db import models
from embed_video.fields import EmbedVideoField

class HomeFields(models.Model):
	logoimg = models.ImageField(upload_to = 'media')
	heading1 = models.CharField(max_length=50)
	heading2 = models.CharField(max_length=100)
	spanheading = models.CharField(max_length=100)
	div2 = models.CharField(max_length=100)
	div2box1 = models.ImageField(upload_to = 'media',default=False)
	div2box2 = models.ImageField(upload_to = 'media',default=False)
	div2box3 = models.ImageField(upload_to = 'media',default=False)
	div2box4 = models.ImageField(upload_to = 'media',default=False)
	video = EmbedVideoField(blank=True)
