FROM python:3.9

WORKDIR /bcfm-api

COPY . .

RUN pip install tk requests Flask 


ENTRYPOINT python app.py


