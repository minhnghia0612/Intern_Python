import pandas as pd
from pydantic import BaseModel, Field

class House(BaseModel):
    area: float
    bedrooms:int
    bathrooms:int
    stories:int
