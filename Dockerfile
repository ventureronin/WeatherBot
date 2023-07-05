FROM python:3.9

# RUN apt-get update && apt-get install -y mysql-server

# WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY loader /app/loader
COPY utils /app/utils
COPY app.py /app/app.py
COPY opt.json /app/opt.json

# RUN service mysql start && mysql -e "CREATE DATABASE my"

#CMD sercive mysql start && python
CMD python /app/app.py
