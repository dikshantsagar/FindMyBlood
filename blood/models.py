# posts/models.py
from django.db import models


class Image(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='static/uploads/')

    def __str__(self):
        return self.title