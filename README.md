<p align="center">
  <img src="https://github.com/matt-novoselov/Linguine-Backend/blob/b9a6f794c6286ffa10ee1c40ce3a817e1ed780b2/LinguineIconRounded.png" alt="Logo" width="80" height="80">
  <h2 align="center">
    Linguine
  </h2>
</p>

Backend code for Linguine - your online language-learning companion, designed to transform education into an enjoyable, gamified experience. Dive into complete lessons and engage in friendly competition with your peers!

<a href="https://youtu.be/bDzZPEOf0J8" target="_blank">
  <img src="https://github.com/matt-novoselov/Linguine-Backend/blob/b9a6f794c6286ffa10ee1c40ce3a817e1ed780b2/LinguineApp.png" alt="GIF">
</a>

## Description
FastAPI on Railway, MySQL on AWS, Cloudflare, Auth0 by Okta, [Frontend](https://github.com/matt-novoselov/Linguine-frontend) !!!!!

![](https://github.com/matt-novoselov/Linguine-Backend/blob/ad7c3867903b89cf02f92b25bdd3b0de3af95106/BackendDiagram.png)

## Requirements
- Python 3.8
- python-dotenv 1.0.0
- aiomysql 0.2.0
- fastapi 0.109.1
- uvicorn 0.23.2

## Installation
1. Clone repository using the following URL: `https://github.com/matt-novoselov/Linguine-Backend.git`
2. Create Environment File:
   - Create a file named `.env` in the root directory of the source folder.
   - Use the provided `.env.example` file as a template.
3. Replace the placeholder values with your specific configuration:
   - HOST: This is the host address for your MySQL database.
   - DB_USERNAME: The username used to access your MySQL database.
   - PASSWORD: The password associated with the provided username for accessing the MySQL database.
   - DATABASE: The name of the MySQL database your bot will use.
4. Build and run using uvicorn `web: uvicorn main:app --host 0.0.0.0 --port $PORT`

<br>

## Credits
Distributed under the MIT license. See **LICENSE** for more information.

Developed with ❤️ by Matt Novoselov
