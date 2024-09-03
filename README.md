<p align="center">
  <img src="https://github.com/matt-novoselov/Linguine-Backend/blob/b9a6f794c6286ffa10ee1c40ce3a817e1ed780b2/LinguineIconRounded.png" alt="Logo" width="80" height="80">
  <h2 align="center">
    Linguine
  </h2>
</p>

Backend code for Linguine - an online language-learning app designed to make education an enjoyable gamified experience. Complete lessons, practice, earn points, and compete with your friends for the highest score!

<a href="https://youtu.be/bDzZPEOf0J8" target="_blank">
  <img src="https://github.com/matt-novoselov/Linguine-Backend/assets/59065228/02f11e91-ef30-4784-91ee-b525a6ad4429" alt="GIF">
</a>

[![](https://github.com/matt-novoselov/matt-novoselov/blob/34555effedede5dd5aa24ae675218d989e976cf6/Files/YouTube_Badge.svg)](https://youtu.be/bDzZPEOf0J8)


## Description
This is a custom backend server developed using **FastAPI**, which is required to manage user registration, score updates, and leaderboard management for the Linguine app. The app utilizes the **API endpoints** of this server to transmit data. Detailed information about the source code of the app can be found in the [Readme file of the Linguine frontend repository](https://github.com/matt-novoselov/Linguine-frontend). Furthermore, detailed instructions on deploying your own Linguine backend server can be found in the [Installation section](#installation).

The server is built using **FastAPI** and includes the following endpoints:

- `/get_stats`: Retrieves statistical data from the database. Returns a **JSON file** with user nicknames and their scores in decreasing order.
- `/get_score/{user_id}`: Retrieves score data for a **specific user** from the database, where `user_id` is a String. Returns the user's score as a String.
- `/update_score/{user_id}/{amount}`: Updates the score for a **specific user** in the database, where `user_id` is a String and `amount` is an Integer. Pass a positive integer to increase the user's score and a negative integer to decrease it. Returns the updated user score as a String. Note that a score cannot go lower than 0.
- `/add_user/{user_id}/{nickname}`: Adds a **new user** to the database, where `user_id` is a String and `nickname` is a String.

For detailed API documentation, please refer to [this link](https://mattapi.fun/docs).

For secure authentication and authorization, the app uses **Auth0**. Auth0 meets all requirements and certificates, including GDPR and HIPAA. The login process involves storing the user’s nickname and score in the database to enable functionality of a leaderboard showcasing top-ranking users. Additionally, sign-in and sign-out functionality help synchronize user progress across various devices.

The backend server connects to a **MySQL database** to store users' scores and nicknames.

![](https://github.com/matt-novoselov/Linguine-Backend/blob/ad7c3867903b89cf02f92b25bdd3b0de3af95106/BackendDiagram.png)

## Requirements
- Python 3.8
- fastapi 0.109.1
- hypercorn 0.17.3
- aiomysql 0.2.0
- python-dotenv 1.0.1

## Installation
1. Clone repository using the following URL: `https://github.com/matt-novoselov/Linguine-Backend.git`
2. Create Environment File:
   - Create a file named `.env` in the root directory of the source folder.
   - Use the provided `.env.example` file as a template.
3. Replace the placeholder values with your specific configuration:
   - API_ROOT_PATH: Root path is `/` my default. Change it if you are using a proxy.
   - DB_HOST: This is the host address for your MySQL database.
   - DB_USERNAME: The username used to access your MySQL database.
   - DB_PASSWORD: The password associated with the provided username for accessing the MySQL database.
   - DB_NAME: The name of the MySQL database your bot will use.
5. Build and run `main.py` using hypercorn. Example: `hypercorn main:app --bind [::]:$PORT3`

<br>

## Credits
Distributed under the MIT license. See **LICENSE** for more information.

Developed with ❤️ by Matt Novoselov
