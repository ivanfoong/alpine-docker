FROM alpine:3.3
MAINTAINER Ivan Foong <vonze21@gmail.com>

RUN apk add --update bind-tools && \
    rm -rf /var/cache/apk/*

ENV S6_OVERLAY_VERSION=v1.17.2.0 GODNSMASQ_VERSION=1.0.2

RUN apk add --update curl && \
    curl -sSL https://github.com/just-containers/s6-overlay/releases/download/${S6_OVERLAY_VERSION}/s6-overlay-amd64.tar.gz \
    | tar xvfz - -C / && \
    curl -sSL https://github.com/janeczku/go-dnsmasq/releases/download/${GODNSMASQ_VERSION}/go-dnsmasq-min_linux-amd64 -o /bin/go-dnsmasq && \
    chmod +x /bin/go-dnsmasq && \
    apk del curl && \
    rm -rf /var/cache/apk/*

ADD root /

ENTRYPOINT ["/init"]
CMD []
