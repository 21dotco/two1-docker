FROM alpine:3.3
MAINTAINER 21.co

RUN apk upgrade -U --available
RUN apk add --no-cache nginx curl

RUN rm /etc/nginx/nginx.conf
RUN rm /etc/nginx/nginx.conf.default

COPY files/nginx.conf /etc/nginx/nginx.conf
CMD nginx -g "daemon off;"
