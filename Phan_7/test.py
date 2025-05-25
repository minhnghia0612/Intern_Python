from fastapi import FastAPI
import asyncio
app = FastAPI()
users = {
    1: {"name": "Alice", "age": 30},
    2: {"name": "Bob", "age": 25},
    3: {"name": "Charlie", "age": 35},
}

async def get_user_from_db(user_id: int):
    await asyncio.sleep(1)
    return {"id": user_id, "name": users[user_id]["name"], "age": users[user_id]["age"]}

async def read():
    await asyncio.sleep(5)
    return  {"massage":"Hello World!"}

# Lấy dữ liệu
@app.get("/")
async def root():
    return await read()

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    user = await get_user_from_db(user_id)
    return user
