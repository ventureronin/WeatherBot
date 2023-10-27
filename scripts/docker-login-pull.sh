#!/bin/bash
# Проверка наличия аргументов
if [ "$#" -ne 2 ]; then
    echo "ERROR\nUsing: $0 missed 2 arguments"
    exit 1
fi

sudo systemctl stop docker.service
sudo apt update
sudo apt install -y docker.io
sudo systemctl start docker.service
sudo usermod -aG docker "$USER"

USERNAME="$1"
PASSWORD="$2"

echo "$PASSWORD" | docker login -u "$USERNAME" --password-stdin
docker pull ventureronin/tg_weatherbot_dev:latest
docker run -d -e TZ=Europe/Kiev ventureronin/tg_weatherbot:latest
