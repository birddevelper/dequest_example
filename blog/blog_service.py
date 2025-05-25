from dequest import sync_client, async_client, QueryParameter, HttpMethod
from blog.dtos import PostDTO


@sync_client(
    dto_class=PostDTO,
    source_field="posts",
    url="https://dummyjson.com/posts",
    method=HttpMethod.GET,
)
def get_posts(query: QueryParameter[str, "q"] = None) -> list[PostDTO]:
    """
    Function to get all posts.
    This function retrieves all posts from the API and returns them as a list of PostDTO objects.
    """
