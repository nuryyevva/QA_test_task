FROM python:3.10.8-slim-bullseye

ENV PYTHONUNBUFFERED 1
WORKDIR /gen
COPY . .
RUN pip install -r requirements.txt
CMD python3 generator.py