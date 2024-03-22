FROM ubuntu:latest
RUN apt update
RUN apt install -y python3
RUN apt install -y python3-pip
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app .
EXPOSE 80
CMD uvicorn app.main:app --host 0.0.0.0 --port 80
