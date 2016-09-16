FROM 21dotco/two1:base
MAINTAINER 21.co

RUN apk add --no-cache linux-headers

WORKDIR /usr/src/app
COPY . ./

RUN pip3 install -e . -U
CMD sh -c "python3 utils/login.py && sleep 2 && python3 server.py"
