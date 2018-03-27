FROM edgarfelizmenio/charm-crypto:latest
MAINTAINER Edgar Felizmenio "edgarfelizmenio@gmail.com"

ADD . /code
WORKDIR /code

RUN apt install -y -q python3-pip

RUN pip3 install -r requirements.txt
RUN pip3 install gunicorn

RUN python3 sample1.py
RUN python3 sample2.py

RUN pip3 freeze