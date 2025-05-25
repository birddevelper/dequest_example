from django.urls import path

from . import views

urlpatterns = [
    path("sync/", views.list_posts, name="sync_posts_list"),
]
