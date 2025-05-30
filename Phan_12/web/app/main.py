import pandas as pd
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request
import joblib
from app.schemas import House

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="static")

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict")
async def predict(house: House):
    try:
        model = joblib.load("app/housing_model.pkl")
        
        input_data = pd.DataFrame([{            
            "area": house.area,
            "bedrooms": house.bedrooms,
            "bathrooms": house.bathrooms,
            "stories": house.stories
        }])
        
        prediction = model.predict(input_data)
        
        return {"predicted_price": prediction[0]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))