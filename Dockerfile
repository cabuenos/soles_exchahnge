FROM python:3.11-slim-bullseye

ARG SLACK_SIGNING_SECRET
ARG SLACK_BOT_TOKEN
ARG SLACK_SOCKET_APP_TOKEN

ENV SLACK_SIGNING_SECRET=$SLACK_SIGNING_SECRET
ENV SLACK_BOT_TOKEN=$SLACK_BOT_TOKEN
ENV SLACK_SOCKET_APP_TOKEN=$SLACK_SOCKET_APP_TOKEN

RUN apt update && apt install cron vim -y

RUN useradd -m -d /opt/home slack

WORKDIR /opt/home

USER slack

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ./src/ .

# cosas para cron
RUN /bin/bash ./utils/scripts/cron.sh
# RUN /bin/bash ./utils/scripts/dolar.py


