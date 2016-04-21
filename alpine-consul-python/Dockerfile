FROM ivanfoong/alpine-consul-base:latest
MAINTAINER Ivan Foong <vonze21@gmail.com>

RUN apk add --update git curl make gcc g++ python linux-headers libgcc libstdc++ binutils-gold python-dev py-pip build-base openssl ca-certificates && \
    pip install -U `pip list --outdated | awk '{ print $1}'` && \
    pip install virtualenv && \
    apk del gcc g++ linux-headers libgcc libstdc++ binutils-gold && \
    rm -rf /var/cache/apk/*