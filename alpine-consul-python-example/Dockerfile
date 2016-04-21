FROM ivanfoong/alpine-consul-python

WORKDIR /app
COPY /app /app
# RUN virtualenv /env && /env/bin/pip install -r /app/requirements.txt
EXPOSE 4000
CMD ["python", "/app/server.py"]