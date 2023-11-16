import os
import asyncio
import aiomysql
from aiomysql import Error
from dotenv import load_dotenv
import json

load_dotenv()
# - - - - - - - - - - #
loop = asyncio.get_event_loop()


async def connect_db():
    try:
        connection = await aiomysql.connect(
            host=os.getenv("HOST"),
            port=24021,
            user=os.getenv("DB_USERNAME"),
            password=os.getenv("PASSWORD"),
            db=os.getenv("DATABASE"),
            loop=loop,
        )

        if connection:
            return connection
        else:
            raise Exception("Database is not connected")

    except Error as e:
        print(f'[!] There was an error in connecting to MySQL Server: {e}')


async def get_cursor():
    global mydb
    try:
        await mydb.ping(reconnect=True)
    except Error:
        mydb = loop.run_until_complete(connect_db())
    return mydb.cursor()


mydb = None


# - - - - - - - - - - #


async def get_stats():
    async with await get_cursor() as cur:
        try:
            #sql = "SELECT JSON_OBJECTAGG(nickname, score) as scores FROM Triolingo ORDER BY score"
            sql = "SELECT nickname, score FROM Triolingo ORDER BY score"
            await cur.execute(sql)
            chart_stats = await cur.fetchall()

            print(chart_stats)

            user_list = [{'name': name, 'score': score} for name, score in chart_stats]

            # Create a dictionary with the 'users' key
            json_data = {'users': user_list}

            # Convert the dictionary to JSON
            json_response = json.dumps(json_data, indent=2)

            # Print or return the JSON response
            print(json_response)

            return json_response

        except Error as e:
            print(f'[!] There was an error in getting stats: {e}')
            pass


async def get_score(selected_user_id: str):
    async with await get_cursor() as cur:
        try:
            query = "SELECT score FROM Triolingo WHERE user_id = %s"
            data_query = (selected_user_id,)
            await cur.execute(query, data_query)
            current_score = await cur.fetchall()  # Get current score
            return current_score[0][0]

        except Error as e:
            print(f'[!] There was an error in trying to get score: {e}')
            pass


async def update_score(user_id: str, amount: int):
    async with await get_cursor() as cur:
        try:
            current_score = await get_score(user_id)

            print(current_score)

            new_score = current_score + amount  # Calculate new score
            if new_score < 0:
                new_score = 0

            print(new_score)

            sql = "UPDATE Triolingo SET score = %s WHERE user_id = %s"
            val = (new_score, user_id)
            await cur.execute(sql, val)
            await mydb.commit()  # Update DB score

            return new_score

        except Error as e:
            print(f'[!] There was an error in updating user score: {e}')
            pass
