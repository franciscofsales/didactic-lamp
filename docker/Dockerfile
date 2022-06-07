FROM python:3.9

LABEL maintainer="Rafael Almeida <rafael@rafaelalmeida.pt>"

RUN apt update && DEBIAN_FRONTEND=noninteractive apt -qq install -y nginx --no-install-recommends

COPY docker/nginx-default.conf /etc/nginx/sites-available/default
COPY html/ /usr/share/nginx/didactic_lamp
COPY python/ /usr/src/app/didactic_lamp

WORKDIR /usr/src/app/didactic_lamp

RUN python -m pip install poetry
RUN python -m pip install --upgrade pip
RUN poetry config virtualenvs.create false
RUN poetry install

WORKDIR /usr/src/app

ENTRYPOINT ["bash", "-c", "/usr/sbin/nginx && python -m uvicorn didactic_lamp.main:app --host=0.0.0.0 --port=8080"]
