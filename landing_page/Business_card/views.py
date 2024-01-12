#from django.http import HttpResponse
from django.shortcuts import render

def rendering_main_page(request):
    return render(request, "index.html")
