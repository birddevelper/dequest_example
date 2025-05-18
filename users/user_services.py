"""
This module contains functions to handle user authentication and retrieval.
we use get_access_token() method to get the access token for the user.
The access token is used to authenticate the user for subsequent API requests.
The get_current_user() method retrieves the current user's information using the access token.
"""

from dequest import sync_client, JsonBody, HttpMethod

from users.dtos import AuthResponseDTO, UserDTO

access_token = None


@sync_client(
    dto_class=AuthResponseDTO,
    url="https://dummyjson.com/auth/login",
    method=HttpMethod.POST,
)
def user_login(username: JsonBody[str], password: JsonBody[str]) -> AuthResponseDTO:
    """
    Function to handle user login.
    """


def get_access_token() -> str:
    """
    Function to get an access token for a user.
    This function retrieves the access token from the API.
    """
    global access_token
    # If the access token is already available, return it
    if access_token:
        print("Access token already available")
        print(f"Access token: {access_token}")
        return access_token

    # Otherwise, perform the login to get a new access token
    print("Access token not available, performing login")
    user_dto = user_login(username="emilys", password="emilyspass")
    access_token = user_dto.accessToken
    print(f"Access token: {access_token}")
    return user_dto.accessToken


@sync_client(
    dto_class=UserDTO,
    url="https://dummyjson.com/auth/me",
    method=HttpMethod.GET,
    auth_token=get_access_token,
)
def get_current_user() -> UserDTO:
    """
    Function to get the current user.
    This function retrieves the current user's information from the API and returns it as a UserDTO object.
    """
