from django.shortcuts import render
from django.http import HttpResponse

from .models import Project

# Create your views here.
def index(request):
    projects = Project.objects.all()[:10]

    context = {
        'title': 'Projects',
        'projects': projects
    }

    return render(request, 'project/index.html', context)