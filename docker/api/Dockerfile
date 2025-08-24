FROM python:3.13-slim
# Install build tools to compile uwsgi
RUN apt-get update && apt-get install -y build-essential gcc && rm -rf /var/lib/apt/lists/*
COPY ./api /app/
RUN pip install --no-cache-dir -r /app/requirements.txt uwsgi
WORKDIR /app
CMD [ "uwsgi", "--die-on-term", "--socket", "127.0.0.1:3031", "--module", "src.app", "--master", "--callable", "app", "--lazy-apps", "--processes", "1", "--threads", "8"]