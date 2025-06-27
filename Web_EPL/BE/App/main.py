from fastapi import FastAPI, Depends, HTTPException, Form
from fastapi.middleware.cors import CORSMiddleware
from . import models,schemas,auth
from sqlalchemy.orm import Session
from .database import get_db,engine
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse
from datetime import timedelta

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["http://localhost:5173"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

@app.post("/user/")
async def create_user(username: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    try:
        existing_user = db.query(models.User).filter(models.User.username == username).first()
        if existing_user:
            raise HTTPException(status_code=400, detail="Username already registered")
        hash_password = auth.get_hash_password(password)
        user = models.User(
            username = username,
            password = hash_password,
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        return JSONResponse(status_code = 201, content = {"message": "User created success", "username": user.username})
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Internal Sever Error")

@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm= Depends(), db: Session= Depends(get_db)):
    user= db.query(models.User).filter(models.User.username == form_data.username).first()
    if not user or not auth.verify_password(form_data.password , user.password):
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    access_token_expires = timedelta(minutes= auth.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = auth.create_access_token(data ={'sub': user.username}, expires_delta=access_token_expires)
    return{"access_token": access_token, "token_type": "bearer"}

@app.post("/logout")
async def logout():
    return JSONResponse(status_code=200, content={"mesage": "Success logout"})

@app.get("/api/rank" , response_model= list[schemas.RankOut])
async def read_rank(db: Session = Depends(get_db)):
    try:
        rank = db.query(models.Rank).all()
        return rank
    except Exception as e:
        print(f"Error rank: {e}")
        raise HTTPException(status_code=500 , detail="Internal Sever Error")
    
@app.get("/api/match/{team_name}", response_model= list[schemas.MatchOut])
async def read_match(team_name: str ,db:Session = Depends(get_db)):
    try:
        matches = db.query(models.Match).filter(models.Match.team_name == team_name).order_by(models.Match.date.asc()).limit(5).all()
        return matches
    except Exception as e:
        print(f"Error match: {e}")
        raise HTTPException(status_code=500, detail="Internal Sever Error")
    
@app.get("/api/player/{player_name}", response_model= list[schemas.PlayerOut])
async def read_player(player_name: str, db:Session = Depends(get_db)):
    try:
        player = db.query(models.Player).filter(models.Player.player_name == player_name).all()
        return player
    except Exception as e:
        print(f"Player error: {e}")
        raise HTTPException(status_code=500, detail="Internal Sever Error")
