FROM edgarfelizmenio/cs300-unified:latest
LABEL maintainer="edgarfelizmenio@gmail.com"

ADD . /code
WORKDIR /code

RUN python3 sample1.py
RUN python3 sample2.py

RUN pip3 freeze