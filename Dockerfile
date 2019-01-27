FROM python:3.7.2-stretch

RUN mkdir -p /app
WORKDIR /app

COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app