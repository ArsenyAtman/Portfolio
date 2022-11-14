from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    title = models.CharField(max_length=200, unique=True)
    preview = models.ImageField(upload_to='images/')
    slug = models.SlugField(max_length=200, unique=True)
    short_description = models.TextField(default="")
    description = models.TextField(default="")
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title