from dequest import (
    sync_client,
    async_client,
    PathParameter,
    QueryParameter,
    HttpMethod,
)
from django.http import JsonResponse
from .dtos import ProductDTO


@sync_client(
    dto_class=ProductDTO,
    url="https://fakestoreapi.com/products/{product_id}",
    method=HttpMethod.GET,
)
def get_product(id: PathParameter[int, "product_id"]) -> ProductDTO:
    """
    Get a product by its ID.
    """


@sync_client(
    dto_class=ProductDTO,
    url="https://fakestoreapi.com/products/",
    method=HttpMethod.GET,
)
def list_product() -> list[ProductDTO]:
    """
    Get products list.
    This function retrieves a list of products from the API and returns them as a list of ProductDTO objects.
    """


def product_callback(response: dict) -> JsonResponse:
    """
    Callback function to handle the response from the async request.
    This function is called when the async request is completed.
    It simply prints the response.
    """
    print("Async request completed. Response:", response)


@async_client(
    # Intentionally not using dto_class here, because we want to return the raw response
    url="https://fakestoreapi.com/products/{product_id}",
    method=HttpMethod.GET,
    callback=product_callback,
)
def get_product_async(
    id: PathParameter[int, "product_id"],
) -> dict:
    """
    Get a product by its ID.
    This function retrieves a product from the API and returns it as a raw json response.
    """
