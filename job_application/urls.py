from tkinter.font import names

from django.urls import path

# from mysite.urls import urlpatterns
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name= "about")
]