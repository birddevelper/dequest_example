from django.http import JsonResponse
from django.shortcuts import render
from blog.blog_service import get_posts


def list_posts(request):
    """
    View to list all blog posts.
    """
    posts = get_posts(query=request.GET.get("q"))

    return JsonResponse(
        {
            "message": "User retrieved successfully",
            "posts": [post.to_json() for post in posts],
        }
    )
