from django.shortcuts import render

from .models import Frontpage

# Create your views here.
def index(request):
    projects = Project.objects.all()[:10]

    context = {
        'title': 'Projects',
        'description': 'A collection of past work',
        'projects': projects
    }

    return render(request, 'project/base_project.html', context)