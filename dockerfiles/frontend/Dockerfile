# FROM gs1-npws_backend:latest as backend

# RUN python /backend/manage.py collectstatic --noinput

###

FROM node:10-slim

RUN apt-get update; apt-get install -y curl gnupg2

RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb http://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list

RUN apt-get update && apt-get install -y --allow-unauthenticated yarn nginx nginx-extras cron && \
  rm -rf /var/lib/apt/lists/* && \
  curl https://dl.eff.org/certbot-auto > /opt/certbot && \
  chmod a+x /opt/certbot  && \
  /opt/certbot --install-only --non-interactive

RUN rm /etc/nginx/sites-enabled/default && \
  rm /etc/nginx/nginx.conf && \
  ln -s /config/nginx/nginx.conf /etc/nginx/sites-enabled/default && \
  ln -s /config/nginx/ssl.conf /etc/nginx/ssl.conf && \
  ln -s /config/nginx/base.conf /etc/nginx/nginx.conf && \
  # chmod a+x /config/letsencrypt/generate.sh && \
  # mkdir -p /etc/letsencrypt && \
  # ln -s /config/letsencrypt/crontab /etc/cron.d/letsencrypt && \
  # chmod 0644 /etc/cron.d/letsencrypt && \
  touch /var/log/cron.log

COPY ./frontend/package.json /frontend/
WORKDIR /frontend
RUN yarn

COPY ./frontend /frontend

RUN yarn build

# CMD /config/letsencrypt/generate.sh
CMD nginx
