from pydantic import BaseModel

class UserOut(BaseModel):
    id: int
    username: str
    #Cho phép lấy tự dộng id và user_name
    class Config:
        orm_mode = True 

class HouseInput(BaseModel):
    area: float
    bedrooms: int
    bathrooms: int
    stories: int

class HouseOutput(BaseModel):
    predicted_price: float