FROM ubuntu:18.04

RUN apt-get update && apt-get install -y \
    python3 python3-dev gcc \
    python3-pip musl-dev g++ \
    libffi-dev openssl

COPY requirements.txt /root/requirements.txt
RUN python3 -m pip install -r /root/requirements.txt

COPY code /usr/local/bin/code