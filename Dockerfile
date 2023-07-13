FROM python:3.9.7

WORKDIR /app
COPY loader/ utils/ app.py config opt.json requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

CMD python app.py
