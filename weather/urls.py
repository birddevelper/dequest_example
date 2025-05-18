from django.urls import path

from . import views

urlpatterns = [
    # Standard APIs
    path("sync", views.sync_weather, name="sync_weather"),
    path("async", views.async_weather, name="async_weather"),
]