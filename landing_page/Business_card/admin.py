from django.contrib import admin
from .models import *

class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("project_name", )}


class SkillAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("skill_name",)}


admin.site.register(Skill)
admin.site.register(Project, ProjectAdmin)
