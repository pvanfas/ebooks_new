from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = "books"

urlpatterns = [
    path("", views.index, name="index"),
]
