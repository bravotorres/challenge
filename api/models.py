import os

from django.core.files.storage import default_storage
from django.db import models

"""
Definitions:
Album:
- Title
- Soft cover / Hard cover
- Photos
- Date of creation

Photo:
- URL of the image
- Caption
- Date of creation

Constraints:
- One Album has many photos and the photo only belongs to one album
"""


class Album(models.Model):
    class Cover(models.TextChoices):
        SOFT = 'Softcover'
        HARD = 'Hardcover'

    title = models.CharField(db_column='Title', max_length=128, blank=False, null=False)
    cover_type = models.CharField(db_column='CoverType', max_length=64, choices=Cover.choices, default=Cover.SOFT)
    creation_at = models.DateTimeField(db_column='Created', auto_now_add=True)
    updated_at = models.DateTimeField(db_column='LastUpdated', auto_now=True)

    class Meta:
        db_table = 'Album'


class Photo(models.Model):
    album_id = models.ForeignKey(Album, on_delete=models.CASCADE)
    url = models.CharField(db_column='URL', max_length=256, blank=False, null=False)
    image = models.ImageField(upload_to=default_storage.path('photos'))
    caption = models.CharField(db_column='Caption', max_length=128)
    created_at = models.DateTimeField(db_column='Created', auto_now_add=True)
    updated_at = models.DateTimeField(db_column='LastUpdated', auto_now=True)
    # image = models.ImageField(db_column='Image', max_length=254, blank=True, null=True)

    class Meta:
        db_table = 'Photo'
