from django.shortcuts import render
from django.http import HttpResponse

from .models import Project, SkillCategory, Skill

def index(request):
    projects = Project.objects.all()[:10]
    skill_categories = SkillCategory.objects.all()

    context = {
        'title': 'Overview',
        'projects': projects,
        'skill_categories': skill_categories
    }

    return render(request, 'base_overview.html', context)

def projects(request):
    projects = Project.objects.all()[:10]

    context = {
        'title': 'Past Projects',
        'projects': projects
    }

    return render(request, 'base_project.html', context)

def project_detail(request, project_id):
    return HttpResponse('Nice, saw project {0}!'.format(project_id))