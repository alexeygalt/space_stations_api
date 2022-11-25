FROM python:3.10-slim

WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
COPY migrations migrations
COPY docker-config.py config.py


CMD flask run -h 0.0.0.0 -p 80