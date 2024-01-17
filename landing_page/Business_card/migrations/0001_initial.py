# Generated by Django 5.0.1 on 2024-01-17 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Skill_block',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='photo/%Y/%m/%d/')),
                ('name_skill', models.TextField()),
                ('details', models.TextField()),
                ('url_sample_work', models.URLField()),
            ],
        ),
    ]
