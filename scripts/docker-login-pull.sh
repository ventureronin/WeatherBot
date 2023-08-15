#!/bin/bash
# Проверка наличия аргументов
if [ "$#" -ne 2 ]; then
    echo "ERROR\nUsing: $0 <username> <password>"
    exit 1
fi

sudo apt update
sudo apt install -y docker.io

# Замените '<ваше_имя_пользователя>' и '<ваш_пароль>' на свои данные
USERNAME="$1"
PASSWORD="$2"

docker login -u "USERNAME" -p "PASSWORD"
#echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin

docker run ventureronin/tg_weatherbot:latest
#docker run -d <имя_контейнера>
echo "Script SUCCSED"