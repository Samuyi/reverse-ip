FROM python:3.10-bookworm

WORKDIR /usr/src/app

RUN chown www-data: /usr/src/app

COPY app.py datastore.py requirements.txt  run.sh ./

RUN pip install -r requirements.txt

RUN chmod +x run.sh

RUN apt update && apt install nginx -y

COPY server.conf  /etc/nginx/sites-available/default

CMD ["/bin/bash", "./run.sh"]

