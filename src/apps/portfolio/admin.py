from django.contrib import admin

from .models import *

class ProjectDocumentInline(admin.StackedInline):
    model = ProjectDocument
    extra = 1

class ProjectImageInline(admin.StackedInline):
    model = ProjectImage
    extra = 2

class FeaturedProjectImageInline(admin.StackedInline):
    model = FeaturedProjectImage
    extra = 0

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ FeaturedProjectImageInline, ProjectImageInline, ProjectDocumentInline ]

class SubSkillInline(admin.StackedInline):
    model = SubSkill
    extra = 1

class SkillAdmin(admin.ModelAdmin):
    inlines = [ SubSkillInline ]

# Register admin modules
admin.site.register(Project, ProjectAdmin)
admin.site.register(SkillCategory)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Activity)
admin.site.register(Honor)
admin.site.register(Job)
admin.site.register(PortfolioConfig)