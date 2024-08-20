from fastapi import FastAPI
import mysql_database

# Initialize FastAPI instance
app = FastAPI()


# Define an event handler for startup event
@app.on_event("startup")
async def _startup():
    # Connect to the MySQL database when the application starts
    mysql_database.mydb = await mysql_database.connect_db()
    print("startup done")


# Define a route to fetch statistics
@app.get('/get_stats')
async def get_stats():
    # Call a function to get statistics data from the database
    stats_data = await mysql_database.get_stats()
    return stats_data


# Define a route to fetch score for a specific user
@app.get('/get_score/{user_id}')
async def get_score(user_id: str):
    # Call a function to get score data for a specific user from the database
    score_data = await mysql_database.get_score(user_id)
    return {"score": score_data}


# Define a route to update score for a specific user
@app.get('/update_score/{user_id}/{amount}')
async def update_score(user_id: str, amount: int):
    # Call a function to update score for a specific user in the database
    score_data = await mysql_database.update_score(user_id, amount)
    return {"score": score_data}


# Define a route to add a new user
@app.get('/add_user/{user_id}/{nickname}')
async def add_user(user_id: str, nickname: str):
    # Call a function to add a new user to the database
    await mysql_database.add_user(user_id, nickname)
