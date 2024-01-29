FROM python:3

ENV PYTHONUNBUFFERED 1
RUN pip install --upgrade pip
WORKDIR /app

COPY . /app

EXPOSE 8000
RUN pip install -r requirements.txt