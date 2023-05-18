FROM python:3-slim

WORKDIR /app
COPY . /app

RUN pip install --no-cache --upgrade pip && \
    pip install --no-cache pymysql langchain openai


