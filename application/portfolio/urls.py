from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('projects/', views.projects, name='projects'),
    path('project/<int:project_id>/', views.project_detail, name='project_detail'),
    path('job/<int:job_id>/', views.job_detail, name='job_detail')
]