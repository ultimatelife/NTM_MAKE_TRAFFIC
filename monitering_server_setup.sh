#!/usr/bin/env bash
add-apt-repository ppa:deadsnakes/ppa -y
apt-get update -y
apt-get install python3.6 nginx git -y

cd /root
git clone https://github.com/ultimatelife/NTM_MAKE_TRAFFIC.git

cd /root/NTM_MAKE_TRAFFIC
systemctl start nginx

curl https://bootstrap.pypa.io/get-pip.py | python3.6
pip3.6 install -r requirements.txt

echo "*/1 * * * * /usr/bin/python3.6 /root/NTM_MAKE_TRAFFIC/make_internet_traffic_public_ip_by_ping.py > /tmp/internet1.log" >> /var/spool/cron/crontabs/root