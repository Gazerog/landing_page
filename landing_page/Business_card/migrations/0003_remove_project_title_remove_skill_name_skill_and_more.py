# Generated by Django 5.0.1 on 2024-01-21 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Business_card', '0002_project_skill_delete_skill_block'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='title',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='name_skill',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='url_sample_work',
        ),
        migrations.AddField(
            model_name='project',
            name='project_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='slug',
            field=models.SlugField(default=''),
        ),
        migrations.AddField(
            model_name='skill',
            name='skill_name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
