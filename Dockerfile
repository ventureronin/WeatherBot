FROM python:3.9.7-slim
RUN mkdir /temp
COPY app/config /temp/
WORKDIR /application/
COPY ./app /application/
RUN --mount=type=secret, id=tg_token && \
    cat /run/secrets/tg_token &&\
    ls -la && \
    pip install --no-cache-dir -r requirements.txt

CMD python app.py
