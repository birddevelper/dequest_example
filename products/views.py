from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET
from products import product_service


def get_product(request, product_id):
    """
    Get a product by its ID.
    """
    product = product_service.get_product(product_id)

    return JsonResponse(
        {
            "message": "Product retrieved successfully",
            "product": product.to_json(),
        }
    )


def product_list(request):
    """
    Get a product by its ID.
    """
    products = product_service.list_product()

    return JsonResponse(
        {
            "message": "Products list retrieved successfully",
            "products": [
                {"id": product.id, "title": product.title} for product in products
            ],
        }
    )


def async_get_product(request, product_id):
    """
    Get a product by its ID asynchronously.
    """
    product = product_service.get_product_async(1)

    return JsonResponse(
        {
            "message": "Request sent asynchronously. Check the console for the response.",
        }
    )
