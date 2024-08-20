import os
import asyncio
import aiomysql
from aiomysql import Error
from dotenv import load_dotenv

# Load secrets from the database
load_dotenv()

# - - - - - - - - - - #
loop = asyncio.get_event_loop()


# Function to connect to the database with a given credentials
async def connect_db():
    try:
        connection = await aiomysql.connect(
            host=os.getenv("DB_HOST"),
            port=int(os.getenv("DB_PORT")),
            user=os.getenv("DB_USERNAME"),
            password=os.getenv("DB_PASSWORD"),
            db=os.getenv("DB_NAME"),
            loop=loop,
        )

        if connection:
            return connection
        else:
            raise Exception("Database is not connected")

    except Error as e:
        print(f'[!] There was an error in connecting to MySQL Server: {e}')


# Function to get database cursor
async def get_cursor():
    global mydb
    try:
        await mydb.ping(reconnect=True)
    except Error:
        mydb = loop.run_until_complete(connect_db())
    return mydb.cursor()


mydb = None
# - - - - - - - - - - #


# Function to get statistics for leaderboard from the database
async def get_stats():
    # Establishing a connection to the database and acquiring a cursor
    async with await get_cursor() as cur:
        try:
            # SQL query to select the nickname and score from the Triolingo table, ordered by score
            sql = "SELECT nickname, score FROM Triolingo ORDER BY score"
            # Executing the SQL query using the cursor
            await cur.execute(sql)
            # Fetching all the results returned by the query
            chart_stats = await cur.fetchall()

            # Creating a list of dictionaries containing usernames and scores from the fetched data,
            # Reversing the order to have the highest scores first
            user_list = [{'name': name, 'score': score} for name, score in chart_stats][::-1]

            # Returning a dictionary containing the user list
            return {'users': user_list}

        except Error as e:
            print(f'[!] There was an error in getting stats: {e}')
            pass


# Function to get score of the particular User by the User ID
async def get_score(selected_user_id: str):
    # Establishing a connection to the database and acquiring a cursor
    async with await get_cursor() as cur:
        try:
            # SQL query to select the score from the Triolingo table for the specified user_id
            query = "SELECT score FROM Triolingo WHERE user_id = %s"
            # Data to be used in the query, in this case, the selected_user_id
            data_query = (selected_user_id,)
            # Executing the SQL query with the provided data
            await cur.execute(query, data_query)
            # Fetching the result of the query, which should be the current score of the selected user
            current_score = await cur.fetchall()
            # Returning the current score (assuming there's only one row returned)
            return current_score[0][0]

        except Error as e:
            print(f'[!] There was an error in trying to get score: {e}')
            pass


# Function to update the score of the particular User by the User ID
async def update_score(user_id: str, amount: int):
    # Establishing a connection to the database and acquiring a cursor
    async with await get_cursor() as cur:
        try:
            # Retrieve the current score of the user
            current_score = await get_score(user_id)

            # Calculate the new score by adding the provided amount to the current score
            new_score = current_score + amount

            # Ensure the new score is not negative
            if new_score < 0:
                new_score = 0

            # SQL query to update the score of the specified user_id in the Triolingo table
            sql = "UPDATE Triolingo SET score = %s WHERE user_id = %s"
            # Values to be used in the query, in this case, the new_score and user_id
            val = (new_score, user_id)
            # Execute the SQL query with the provided values
            await cur.execute(sql, val)
            # Committing the changes to the database
            await mydb.commit()

            print(f"[v] {user_id} updated his score by {amount}")

            # Return the new score after the update
            return new_score

        except Error as e:
            print(f'[!] There was an error in updating user score: {e}')
            pass


# Function to add new user to the database
async def add_user(selected_user_id: str, nickname: str):
    # Establishing a connection to the database and acquiring a cursor
    async with await get_cursor() as cur:
        try:
            # Checking if the user already exists in the database
            query = "select if( exists(select* from Triolingo where user_id = %s), 1, 0)"
            data_query = (selected_user_id,)
            await cur.execute(query, data_query)
            user_exist = await cur.fetchone()
            user_exist = user_exist[0]

            # Add new user if they don't exist in the database
            if not user_exist:
                # SQL query to insert a new user into the Triolingo table
                query = "insert into Triolingo (user_id, nickname) values (%s, %s)"
                data_query = (selected_user_id, nickname)
                # Execute the SQL query with the provided values
                await cur.execute(query, data_query)
                # Committing the changes to the database
                await mydb.commit()

                print(f"[v] {selected_user_id} was added to the database with nickname {nickname}")

        except Error as e:
            print(f'[!] There was an error in trying to add user: {e}')
            pass
