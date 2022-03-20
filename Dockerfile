FROM alpine:latest
RUN apk update && apk add python3 py3-pip gcc musl-dev python3-dev
RUN mkdir /app
RUN pip3 install RPi.GPIO paho-mqtt
COPY gpio.py /app
WORKDIR /app
CMD python3 gpio.py
