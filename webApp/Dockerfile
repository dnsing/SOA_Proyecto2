# Dockerfile

FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8000
EXPOSE 9000
EXPOSE 11000

CMD ["python", "webApp.py"]