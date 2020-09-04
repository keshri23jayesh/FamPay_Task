from django.db import models

# Create your models here.


class videos(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    video_id = models.CharField(max_length=50, unique=True)
    publishedAt = models.TextField()
    video_title = models.TextField(blank=True)
    video_desc = models.TextField(blank=True)
    thumbnail_url = models.TextField(blank=True)

    class Meta:
        db_table = 'VIDEOS'
