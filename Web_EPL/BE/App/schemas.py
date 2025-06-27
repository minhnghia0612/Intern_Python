from pydantic import BaseModel
from datetime import date

class TeamOut(BaseModel):
    name: str
    logo: str

    class Config:
        orm_mode = True

class RankOut(BaseModel):
    id: int
    rank: int
    team: TeamOut
    matched_played: int
    win: int
    draw: int
    lose: int
    gd: int
    points: int
    
    class Config:
        orm_mode = True

class PlayerOut(BaseModel):
    id: int
    player_name: str
    player_url: str
    nation : str
    pos: str
    age: int
    mp: int
    starts: int
    minutes: int
    team: TeamOut

    class Config:
        orm_mode = True

class MatchOut(BaseModel):
    id: int
    date: date   
    venue: str
    gf: int
    ga: int
    opponent: str
    team: TeamOut

    class Config:
        orm_mode = True          