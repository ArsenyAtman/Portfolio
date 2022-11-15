from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    title = models.CharField(max_length=200, unique=True)
    preview = models.ImageField(upload_to='images/', blank=True)
    slug = models.SlugField(max_length=200, unique=True)
    short_description = models.TextField(default="")
    description = models.TextField(default="")
    created_on = models.DateTimeField(auto_now_add=True)
    youtube_link = models.CharField(max_length=200, default='', blank=True)
    github_link = models.CharField(max_length=200, default='', blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

class About(models.Model):
    name = models.CharField(max_length=200, unique=True)
    photo = models.ImageField(upload_to='images/', blank=True)
    experience = models.TextField(default="")
    skills = models.TextField(default="")
    linkedin_link = models.CharField(max_length=200, default='', blank=True)
    github_link = models.CharField(max_length=200, default='', blank=True)

    def __str__(self):
        return self.name