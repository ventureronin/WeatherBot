FROM python:3.9.7-slim

WORKDIR /application/
COPY ./app /application/
ARG config
ARG json
ENV config=$config
ENV json=$json
RUN echo $config > /application/config && \
    echo "$json" > /application/opt.json && \
    pip install --no-cache-dir -r requirements.txt && \
    sudo apt install nano

CMD python app.py
