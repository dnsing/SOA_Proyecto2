# Dockerfile

FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 9000
EXPOSE 10000

CMD ["python", "img_analyzer.py"]