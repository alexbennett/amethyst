from django.utils import timezone
from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    abstract = models.TextField()
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now(), blank=True)

    def __str__(self):
        return self.title

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/%Y/%m/%d')

    def __str__(self):
        return 'Image'

class SkillCategory(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=200)
    projects = models.ManyToManyField(Project, blank=True)
    category = models.ForeignKey(SkillCategory, related_name='skills', on_delete=models.CASCADE)
    more_info = models.TextField(blank=True )
    slug = models.SlugField(max_length=8, unique=True)

    def __str__(self):
        return self.name

class SubSkill(models.Model):
    name = models.CharField(max_length=24)
    skills = models.OneToOneField(Skill, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, related_name='sub_skills', on_delete=models.CASCADE)
    category = models.ForeignKey(SkillCategory, related_name='sub_skills', on_delete=models.CASCADE)

    def __str__(self):
        return self.name