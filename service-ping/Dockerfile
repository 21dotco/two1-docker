FROM 21dotco/two1:base
MAINTAINER 21.co

RUN apk add --no-cache linux-headers

WORKDIR /usr/src/app
COPY . ./

RUN pip3 install -e . -U

COPY ping-entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/ping-entrypoint.sh
ENTRYPOINT ["ping-entrypoint.sh"]
