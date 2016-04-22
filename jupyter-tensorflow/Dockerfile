FROM ivanfoong/alpine-consul-python

ADD repositories /etc/apk/repositories
RUN apk add --update gfortran py-scipy@testing py-scipy-dev@testing py-numpy@testing py-numpy-dev@testing

ADD root /

RUN pip install --no-cache-dir -r /app/requirements.txt

RUN mkdir -p /notebooks
WORKDIR /notebooks