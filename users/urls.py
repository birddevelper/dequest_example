from django.urls import path

from . import views

urlpatterns = [
    path("sync/", views.get_current_user, name="sync_user_retrieve"),
]
