from django.shortcuts import render
from django.views import generic
from .models import Project, About

class ProjectList(generic.ListView):
    queryset = Project.objects.order_by('-created_on')
    template_name = 'index.html'

class ProjectDetail(generic.DetailView):
    model = Project
    template_name = 'project_detail.html'

class AboutDetail(generic.ListView):
    model = About
    template_name = 'about.html'