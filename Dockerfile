#FROM python:3.8.5

FROM python:3.8-slim-buster

COPY requirements.txt requirements.txt 

RUN pip3 install --upgrade pip3 && pip3 install -r requirements.txt

COPY code code

ENTRYPOINT [ "./code/main.sh" ]