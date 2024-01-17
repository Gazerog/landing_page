from django.urls import path
from .views import *

urlpatterns = [
    path("", rendering_pages,kwargs={"name": "home"}, name='home'),
    path("about/", rendering_pages,kwargs={"name": "about"}, name='about'),
    path("serices/", rendering_pages,kwargs={"name": "service"}, name='service'),
    path("github/", rendering_pages,kwargs={"name": "github"}, name='github'),
]

