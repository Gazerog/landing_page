from django.db import models

class Project(models.Model):
    screenshot = models.ImageField(upload_to="photo/%Y/%m/%d/")
    project_name = models.CharField(max_length=255, null=True)
    details = models.TextField()
    slug = models.SlugField(default="", null=False)

class Skill(models.Model):
    logo = models.ImageField(upload_to="photo/%Y/%m/%d/")
    skill_name = models.CharField(max_length=255, null=True)
    details = models.TextField()
    tematic_project = models.ManyToManyField(Project)
    slug = models.SlugField(default="", null=False)


