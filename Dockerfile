FROM python:3.9.7-slim
RUN mkdir /temp
COPY app/config /temp/
WORKDIR /application/
COPY ./app /application/
RUN ls -la && \
    pip install --no-cache-dir -r requirements.txt

CMD python app.py
