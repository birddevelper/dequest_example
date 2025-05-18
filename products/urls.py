from django.urls import path

from . import views

urlpatterns = [
    path("sync/<int:product_id>", views.get_product, name="sync_products_retrieve"),
    path("sync/", views.product_list, name="sync_products_list"),
    path(
        "async/<int:product_id>",
        views.async_get_product,
        name="async_products_retrieve",
    ),
]
