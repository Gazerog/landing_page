from django.urls import path
from .views import *

urlpatterns = [
    path("", rendering_main_page),
]

