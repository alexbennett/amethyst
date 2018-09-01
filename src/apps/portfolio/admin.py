from django.contrib import admin

from .models import Project, ProjectImage, Skill, SkillCategory, SubSkill

class ProjectImageInline(admin.StackedInline):
    model = ProjectImage
    extra = 2

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ ProjectImageInline ]

class SkillInline(admin.StackedInline):
    model = Skill
    extra = 3

class SubSkillInline(admin.StackedInline):
    model = SubSkill
    extra = 1

class SkillCategoryAdmin(admin.ModelAdmin):
    inlines = [ SkillInline, SubSkillInline ]

admin.site.register(Project, ProjectAdmin)
admin.site.register(SkillCategory, SkillCategoryAdmin)