from fastapi import FastAPI
import mysql_database
import json

app = FastAPI()  # --reload


@app.on_event("startup")
async def _startup():
    mysql_database.mydb = await mysql_database.connect_db()
    print("startup done")


@app.get('/get_stats')
async def get_stats():
    stats_data = await mysql_database.get_stats()
    return stats_data


@app.get('/get_score/{user_id}')
async def get_score(user_id: str):
    score_data = await mysql_database.get_score(user_id)
    return {"score": score_data}


@app.patch('/update_score/{user_id}/{amount}')
async def update_score(user_id: str, amount: int):
    score_data = await mysql_database.update_score(user_id, amount)
    return score_data
