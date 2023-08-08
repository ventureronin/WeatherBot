FROM python:3.9.7-slim

WORKDIR /application/
COPY ./app /application/
ARG config
ARG json
ENV config=$config
ENV json=$json
RUN echo $config > /application/config && \
    echo '$json base64' -d > /application/opt.json && \
    cat /application/opt.json && \
    ls -la && \
    pip install --no-cache-dir -r requirements.txt

CMD python app.py
