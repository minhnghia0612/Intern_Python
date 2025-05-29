from pydantic import BaseModel
from typing import Optional

class House(BaseModel):
    area: float
    bedrooms: int
    bathrooms: int
    stories: int