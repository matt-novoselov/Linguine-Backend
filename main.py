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
    return json.loads(stats_data)


@app.get('/get_score/{name}')
async def get_stats(name: str):
    score_data = await mysql_database.get_score(name)
    return score_data

@app.get('/update_score/{name}/{amount}')
async def get_stats(name: str, amount: int):
    score_data = await mysql_database.update_score(name, amount)
    return score_data