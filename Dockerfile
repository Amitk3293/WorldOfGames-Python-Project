# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements-flask.txt requirements.txt

RUN pip3 install -r requirements.txt
RUN echo "This Flask in running on port 5000"

COPY MainScores.py .

EXPOSE 5000

CMD [ "python3", "MainScores.py" ]

