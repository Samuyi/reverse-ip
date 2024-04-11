gunicorn --bind 127.0.0.1:3000 --workers=2 app:app --daemon -u www-data
nginx -g 'daemon off;'