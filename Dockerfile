FROM ubuntu:latest
RUN apt update && apt install -y python3 && apt install -y python3-pip && apt install -y nginx && apt install -y supervisor
WORKDIR /app
RUN mkdir app
RUN rm -rf /etc/nginx/sites-enabled/*
COPY nginx.conf /etc/nginx/sites-enabled/
COPY requirements.txt .
COPY app ./app
COPY supervisord.conf .
RUN pip install --no-cache-dir -r  requirements.txt
EXPOSE 80
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3\
    CMD curl -f http://localhost:80/ || exit 1
CMD supervisord -c supervisord.conf