from django.shortcuts import render
from django.http import HttpResponse

from .models import Project, SkillCategory, Skill, Activity, Honor, Job


def index(request):
    projects = Project.objects.all()
    skill_categories = SkillCategory.objects.all()
    skills = Skill.objects.all()
    activities = Activity.objects.all()
    honors = Honor.objects.all()
    jobs = Job.objects.all()

    context = {
        'title': 'Overview',
        'projects': projects,
        'skill_categories': skill_categories,
        'skills': skills,
        'activities': activities,
        'honors': honors,
        'jobs': jobs
    }

    return render(request, 'base_overview.html', context)


def projects(request):
    projects = Project.objects.all()

    context = {
        'title': 'Projects',
        'projects': projects
    }

    return render(request, 'base_projects.html', context)


def project_detail(request, project_id):
    projects = Project.objects.all()

    # Get project by id
    try:
        project_obj = Project.objects.get(id=project_id)
    except Project.DoesNotExist:
        return HttpResponse("Project not found")

    context = {
        'title': 'Project Summary',
        'project': project_obj,
        'projects': projects
    }

    return render(request, 'base_project_detail.html', context)
