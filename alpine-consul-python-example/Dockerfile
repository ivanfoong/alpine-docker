FROM ivanfoong/alpine-consul-python

ADD root /
WORKDIR /app
RUN pip install --no-cache-dir -r /app/requirements.txt
EXPOSE 4000