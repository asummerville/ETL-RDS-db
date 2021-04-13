FROM python:3.8.5

COPY requirements.txt requirements.txt 

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY code code

ENTRYPOINT [ "./code/main.sh" ]