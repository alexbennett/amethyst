from django.shortcuts import render
from django.http import HttpResponse

from .models import Project, SkillCategory, Skill, Activity, Honor, Job, Education


def index(request):
    projects = Project.objects.all()
    skill_categories = SkillCategory.objects.all()
    skills = Skill.objects.all()
    activities = Activity.objects.all()
    honors = Honor.objects.all()
    jobs = Job.objects.all()
    educations = Education.objects.all()

    context = {
        'title': 'Overview',
        'projects': projects,
        'skill_categories': skill_categories,
        'skills': skills,
        'activities': activities,
        'honors': honors,
        'jobs': jobs,
        'educations': educations
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
    # Get all projects (for header information)
    projects = Project.objects.all()

    # Get specific project by id
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

def job_detail(request, job_id):
    # Get all projects (for header information)
    projects = Project.objects.all()

    # Get specific job by id
    try:
        job_obj = Job.objects.get(id=job_id)
    except Job.DoesNotExist:
        return HttpResponse("Job not found")

    context = {
        'title': 'Job Summary',
        'projects': projects,
        'job': job_obj
    }
    
    return render(request, 'base_job_detail.html', context)

