from django.http import JsonResponse
from users import user_services


def get_current_user(request):
    """
    Get the current user.
    """
    user = user_services.get_current_user()

    return JsonResponse(
        {
            "message": "User retrieved successfully",
            "user": user.to_json(),
        }
    )
