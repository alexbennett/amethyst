from django.contrib import admin

from .models import *

class ProjectVideoInline(admin.StackedInline):
    model = ProjectVideo
    extra = 1

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
    inlines = [ FeaturedProjectImageInline, ProjectImageInline, ProjectVideoInline, ProjectDocumentInline ]

class SubSkillInline(admin.StackedInline):
    model = SubSkill
    extra = 1

class SkillAdmin(admin.ModelAdmin):
    inlines = [ SubSkillInline ]

class JobImageInline(admin.StackedInline):
    model = JobImage
    extra = 2

class JobAdmin(admin.ModelAdmin):
    inlines = [ JobImageInline ]

# Register admin modules
admin.site.register(Project, ProjectAdmin)
admin.site.register(SkillCategory)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Activity)
admin.site.register(Honor)
admin.site.register(Job, JobAdmin)
admin.site.register(PortfolioConfig)
admin.site.register(Education)