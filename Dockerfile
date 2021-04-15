FROM python:3.8.5

#FROM python:3.8-slim-buster

COPY requirements.txt requirements.txt 

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY code .

ENTRYPOINT [ "./main.py" ]