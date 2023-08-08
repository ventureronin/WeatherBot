FROM python:3.9.7-slim

WORKDIR /application/
COPY ./app /application/
RUN --mount=type=secret,id=tg_token \
    cat /run/secrets/tg_token && \
    cat /run/secrets/tg_token && \
    mv /run/secrets/tg_token /application/config && \
    ls -la && \
    pip install --no-cache-dir -r requirements.txt

CMD python app.py
