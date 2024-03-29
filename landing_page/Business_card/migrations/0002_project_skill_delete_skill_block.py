# Generated by Django 5.0.1 on 2024-01-18 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Business_card', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('screenshot', models.ImageField(upload_to='photo/%Y/%m/%d/')),
                ('title', models.CharField(max_length=30)),
                ('details', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='photo/%Y/%m/%d/')),
                ('name_skill', models.CharField(max_length=30)),
                ('details', models.TextField()),
                ('url_sample_work', models.URLField(max_length=10)),
                ('tematic_project', models.ManyToManyField(to='Business_card.project')),
            ],
        ),
        migrations.DeleteModel(
            name='Skill_block',
        ),
    ]
