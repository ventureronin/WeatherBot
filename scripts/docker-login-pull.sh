#!/bin/bash
# Проверка наличия аргументов
if [ "$#" -ne 2 ]; then
    echo "ERROR\nUsing: $0 <username> <password>"
    exit 1
fi

sudo apt update
sudo apt install -y docker.io
sudo usermod -aG docker "$USER"

USERNAME="$1"
PASSWORD="$2"

echo "$PASSWORD" | docker login -u "$USERNAME" --password-stdin

docker run -d ventureronin/tg_weatherbot:latest