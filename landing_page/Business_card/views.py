from django.shortcuts import render, get_object_or_404
from .models import *

def rendering_pages(request, name):
    return render(request, f"{name}.html")

#def create_context_for_bth_skill_box():
#    menu = Skill.objects.all()
#    for i in menu:
#        print(i.tematic_project.get(id=1).slug)
#    return menu

def home_page_rendering(request):
    all_skills = Skill.objects.all()
    return render(request, 'home.html', context={'block_menu': all_skills})

def skill_page_rendering(request, skill_slug):
    skill = get_object_or_404(Skill, slug=skill_slug)
    context = {"title": skill.skill_name}
    return render(request, "service.html", context=context)

def project_page_rendering(request, slug):
    pass


