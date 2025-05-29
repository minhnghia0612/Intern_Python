from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import numpy as np
import joblib
from . import schemas

app = FastAPI()

#read file train 
#rb is read binary
with open("app/housing_model.pkl", "rb") as f:
    model = joblib.load(f)    

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Housing Price Prediction API"}

@app.post("/predict")
async def predict(house: schemas.House):
    input_data = np.array([[house.area, house.bedrooms, house.bathrooms, house.stories]])
    prediction = model.predict(input_data)[0]
    return {"prediction": float(prediction)}    