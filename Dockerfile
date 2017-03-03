FROM docker.made.com/ops/alpine-s6:3.4-1

COPY requirements.txt ./

RUN apk --update upgrade && apk add python3 libpq xmlsec@made

RUN pip3 install -r requirements.txt

RUN apk --update upgrade && apk add  python3-dev && \
    pip3 install -r requirements.txt


COPY . ./

RUN mkdir -p /etc/consul-template/conf.d

CMD "./entrypoint.sh"
