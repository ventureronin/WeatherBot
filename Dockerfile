FROM python:3.9.7-slim
WORKDIR /application/
COPY /app/loader/ /app/utils /app/requirements.txt /app/app.py/ /app/config /app/opt.json ./application
RUN ls -la && \
    pip install --no-cache-dir -r requirements.txt

CMD python app.py
