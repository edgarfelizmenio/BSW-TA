FROM ubuntu:16.04
MAINTAINER Edgar Felizmenio "edgarfelizmenio@gmail.com"

ADD . /code
WORKDIR /code

RUN apt update && apt install --yes build-essential flex bison wget subversion m4 python3 python3-dev python3-setuptools libgmp-dev libssl-dev
RUN wget https://crypto.stanford.edu/pbc/files/pbc-0.5.14.tar.gz && tar xvf pbc-0.5.14.tar.gz && cd pbc-0.5.14 && ./configure LDFLAGS="-lgmp" && make && make install && ldconfig
WORKDIR charm
RUN ./configure.sh && make && make install && ldconfig

RUN apt install -y -q python3-pip

# RUN apt-get update -y -q 
# RUN apt-get upgrade -y -q
# RUN apt-get install -y -q --no-install-recommends apt-utils
# RUN apt-get install -y -q lzip
# RUN apt-get install -y -q build-essential
# RUN apt-get install -y -q m4
# RUN apt-get install -y -q flex bison
# RUN apt-get install -y -q python3-setuptools
# RUN apt-get install -y -q python3-dev

# # Install GMP
# RUN tar --lzip -xvf gmp-6.1.2.tar.lz;
# # RUN tar -xvf gmp-6.1.2.tar.lz;
# WORKDIR gmp-6.1.2
# RUN ./configure;
# RUN make;
# RUN make check;
# RUN make install; # sudo make install

# # Install PBC from source
# WORKDIR /code
# RUN tar -xvf pbc-0.5.14.tar.gz
# WORKDIR pbc-0.5.14
# RUN ./configure
# RUN ./configure LDFLAGS="-lgmp"
# RUN make
# RUN make install
# RUN ldconfig

# # Install OpenSSL

# WORKDIR /code
# RUN tar -xvf openssl-1.1.0g.tar.gz
# WORKDIR openssl-1.1.0g
# RUN ./config
# RUN make
# RUN sudo make test
# RUN make install
# RUN ldconfig

# # Now we can build and install Charm:
# WORKDIR /code
# RUN pip3 install --upgrade setuptools

# WORKDIR charm
# RUN ./configure.sh
# RUN make install
# RUN make test

WORKDIR /code

RUN pip3 install -r requirements.txt
RUN pip3 install gunicorn

RUN python3 sample1.py
RUN python3 sample2.py

RUN pip3 freeze