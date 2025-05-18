from django.urls import path

from . import views

urlpatterns = [
    # Standard APIs
    path("", views.index, name="index"),
]