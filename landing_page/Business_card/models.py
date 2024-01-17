from django.db import models

class Skill_block(models.Model):
    logo = models.ImageField(upload_to="photo/%Y/%m/%d/")
    name_skill = models.TextField()
    details = models.TextField()
    url_sample_work = models.URLField()
