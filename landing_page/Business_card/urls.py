from django.urls import path
from .views import *

urlpatterns = [
    path("", home_page_rendering , name='home'),
    path("about/", rendering_pages,kwargs={"name": "about"}, name='about'),
    path("services/", rendering_pages,kwargs={"name": "service"}, name='services'),
    path("github/", rendering_pages,kwargs={"name": "github"}, name='github'),
    path("services/<slug:skill_slug>/", skill_page_rendering, name="service"),
    path("services/<slug:project_slug>/", project_page_rendering),
]

