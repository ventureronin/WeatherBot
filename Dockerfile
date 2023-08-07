FROM python:3.9.7-slim
RUN mkdir /application/
WORKDIR /application/
COPY ./app /application/.
RUN ls -la > /application/test.txt && \
    cat /application/test.txt && \
    pip install --no-cache-dir -r requirements.txt

CMD python app.py
