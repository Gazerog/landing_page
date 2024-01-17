from django.shortcuts import render
from .models import *

def rendering_pages(request, name):
    if name == 'home':
        menu_skill_blocks = Skill_block.objects.all()
        return render(request, "home.html", context={'block_menu': menu_skill_blocks})
    return render(request, f"{name}.html")

