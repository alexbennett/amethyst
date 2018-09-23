from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.contrib.sites.models import Site


class PortfolioConfig(models.Model):
    site = models.OneToOneField(Site, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    biography = models.TextField(blank=True)

    def __str__(self):
        return "Portfolio configuration (" + self.title + ")"


class Project(models.Model):
    title = models.CharField(max_length=200)
    abstract = RichTextField()
    description = RichTextField()
    created_at = models.DateTimeField(blank=True)
    logo = models.ImageField(upload_to='img/projects/logos', blank=True)

    def __str__(self):
        return self.title


class ProjectImage(models.Model):
    project = models.ForeignKey(
        Project, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='img/projects')

    def __str__(self):
        return 'Project image'


class FeaturedProjectImage(models.Model):
    project = models.ForeignKey(
        Project, related_name='featured_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='img/projects/featured')

    def __str__(self):
        return 'Featured project image'


class ProjectDocument(models.Model):
    project = models.ForeignKey(
        Project, related_name='documents', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class SkillCategory(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "skill categories"


class Skill(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(
        SkillCategory, related_name='skills', on_delete=models.CASCADE)
    more_info = models.TextField(blank=True)
    related_projects = models.ManyToManyField(Project, blank=True)
    related_jobs = models.ManyToManyField("Job", blank=True)
    slug = models.SlugField(max_length=8, unique=True)

    def __str__(self):
        return self.name


class SubSkill(models.Model):
    name = models.CharField(max_length=24)
    parent_skill = models.ForeignKey(Skill, related_name='sub_skills', on_delete=models.CASCADE)
    #category = models.ForeignKey(SkillCategory, related_name='sub_skills', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Activity(models.Model):
    title = models.CharField(max_length=200)
    organization = models.CharField(max_length=100)
    organization_url = models.CharField(max_length=200, blank=True)
    when = models.CharField(max_length=20)

    def __str__(self):
        return self.title + " (" + self.organization + ")"

    class Meta:
        verbose_name_plural = "activities"


class Honor(models.Model):
    title = models.CharField(max_length=200)
    organization = models.CharField(max_length=100)
    when = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Job(models.Model):
    title = models.CharField(max_length=100)
    employer = models.CharField(max_length=100)
    description = RichTextField()
    location = models.CharField(blank=True, max_length=100)
    started = models.DateField()
    ended = models.DateField()
    current = models.BooleanField(default=False) 
    logo = models.ImageField(upload_to='img/jobs/logos', blank=True)

    def __str__(self):
        return self.title + " (" + self.employer + ")"


class JobImage(models.Model):
    job = models.ForeignKey(
        Job, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='img/jobs')

    def __str__(self):
        return 'Job image'


class Education(models.Model):
    degree = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    started = models.DateField()
    ended = models.DateField()

    def __str__(self):
        return self.degree + " (" + self.school + ")"
