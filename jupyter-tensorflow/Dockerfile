FROM ivanfoong/alpine-consul-python

ADD repositories /etc/apk/repositories
RUN apk add --update gfortran py-scipy@testing py-scipy-dev@testing py-numpy@testing py-numpy-dev@testing

ADD /app /app
RUN pip install -r /app/requirements.txt

RUN mkdir -p /notebooks
WORKDIR /notebooks

CMD ["exec", "jupyter", "notebook", "/notebooks", "--port=8888", "--ip=0.0.0.0", "--no-browser"]