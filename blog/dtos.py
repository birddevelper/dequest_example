from dataclasses import dataclass
from typing import List


@dataclass
class ReactionsDTO:
    likes: int
    dislikes: int

    def to_json(self) -> dict:
        """
        Convert the ReactionsDTO instance to a JSON serializable dictionary.
        """
        return {"likes": self.likes, "dislikes": self.dislikes}


@dataclass
class PostDTO:
    id: int
    title: str
    body: str
    tags: List[str]
    reactions: ReactionsDTO
    views: int
    userId: int

    def to_json(self) -> dict:
        """
        Convert the PostDTO instance to a JSON serializable dictionary.
        """
        return {
            "id": self.id,
            "title": self.title,
            "body": self.body,
            "tags": self.tags,
            "reactions": self.reactions.to_json(),
            "views": self.views,
            "userId": self.userId,
        }
