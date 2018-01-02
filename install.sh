#! /bin/bash -x

apt-get -y -q update
apt-get -y -q upgrade
apt-get -y -q install htop
apt-get -y -q install build-essential
apt-get -y -q install git
apt-get -y -q install vim

apt-get install -y -q lzip
apt-get install -y -q flex bison
apt-get install -y -q python3-setuptools
apt-get install -y -q python3-dev
apt-get install -y -q python3.4-venv

apt-get -y -q install nginx

debconf-set-selections <<< 'mysql-server-5.6 mysql-server/root_password password password'
debconf-set-selections <<< 'mysql-server-5.6 mysql-server/root_password_again password password'
apt-get -y -q install mysql-server-5.6 mysql-client-5.6

cd ../BSW-TA

mysql --user=root --password=password --execute="CREATE DATABASE raw_ta"
mysql --user=root --password=password raw_ta --execute="source raw_ta.sql"

# Install GMP
tar --lzip -xvf gmp-6.1.2.tar.lz;
cd gmp-6.1.2;
./configure;
make;
make check;
make install; # sudo make install

# Install PBC from source
cd ..
tar -xvf pbc-0.5.14.tar.gz
cd pbc-0.5.14
./configure
./configure LDFLAGS="-lgmp"
make
make install
ldconfig

# Install OpenSSL

cd ..
tar -xvf openssl-1.1.0g.tar.gz
cd openssl-1.1.0g
./config
make
make test
make install
ldconfig

# Now we can build and install Charm:
cd ..
python3 -m venv env
source env/bin/activate
pip3 install --upgrade setuptools

cd charm
./configure.sh
make install
make test

cd ..
pip3 install -r requirements.txt

python3 sample1.py
python3 sample2.py

pip3 freeze

# install gunicorn
# pip3 install gunicorn

# install and enable nginx
# cp nginx/source-shr /etc/nginx/sites-available/source-shr
# ln -s /etc/nginx/sites-available/source-shr /etc/nginx/sites-enabled/source-shr
# sudo service nginx restart

# start the mediator
# cp upstart/source-shr.conf /etc/init/source-shr.conf
# sudo service source-shr start