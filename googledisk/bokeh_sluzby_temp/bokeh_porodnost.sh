bokeh serve --ssl-certfile /etc/letsencrypt/live/geografieliberec.cz/cert.pem --ssl-keyfile /etc/letsencrypt/live/geografieliberec.cz/privkey.pem --show --allow-websocket-origin="*" --port 5010 /var/www/html/mapy/published/01-bokeh/bokeh_porodnost.py