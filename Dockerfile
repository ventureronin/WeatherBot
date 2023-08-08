FROM python:3.9.7-slim

WORKDIR /application/
COPY ./app /application/
ARG config
ENV config=$config
RUN cat $config > /application/config && \
    ls -la && \
    pip install --no-cache-dir -r requirements.txt

CMD python app.py
