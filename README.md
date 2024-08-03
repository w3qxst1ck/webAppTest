# Telegram bot with test web api #

#### This project has implemented docker-compose file which consists of 4 containers: ####
#### 1. Nginx container which accepts 80 port and proxy to container with api ####
#### 2. Api which accepts 8000 and have two endpoints for create and retrieve messages (with post and get http requests) ####
#### 3. MongoDB container contains database for storing records ####
#### 4. TgBot container contains code base for python aiogram3 telegram bot which refers to nginx container by container name and 80 port. List of messages has pagination and telegram id of sender ####

#### Telegram bot link: @TestTaskMessageBot ####

Start command to run app with docker compose:
```
$ docker-compose up --buid -d
```