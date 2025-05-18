from dataclasses import asdict, dataclass
from typing import Optional


@dataclass
class ProductRatingDTO:
    rate: float
    count: int

    def to_json(self):
        return asdict(self)


@dataclass
class ProductDTO:
    id: int
    title: str
    price: float
    description: str
    category: str
    image: str
    rating: Optional[ProductRatingDTO] = None

    def to_json(self):
        return asdict(self)
