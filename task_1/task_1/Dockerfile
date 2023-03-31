FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt ./

RUN apt-get update -y && \
    pip install -r requirements.txt

COPY . .

EXPOSE 9999

CMD [ "python3", "api.py" ]