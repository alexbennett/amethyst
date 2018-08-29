from django.shortcuts import render
from django.http import HttpResponse

from .models import Project

def index(request):
    return HttpResponse('Nice!')

def projects(request):
    projects = Project.objects.all()[:10]

    context = {
        'title': 'Projects',
        'projects': projects
    }

    return render(request, 'base_project.html', context)

def project_detail(request, project_id):
    return HttpResponse('Nice, saw project {0}!'.format(project_id))