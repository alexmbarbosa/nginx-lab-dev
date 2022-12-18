FROM nginx

COPY ./files/conf/nginx.conf /etc/nginx/nginx.conf
COPY ./files/conf/conf.d /etc/nginx/conf.d
COPY ./files/static /usr/share/nginx/html