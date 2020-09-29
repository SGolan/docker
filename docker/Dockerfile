from ubuntu

run ln -fs /usr/share/zoneinfo/America/New_York /etc/localtime

run apt-get update
run apt-get install -y python3
run apt-get install -y python3-pip
run apt-get install -y python3-tk

run pip3 install pyqt5
run pip3 install matplotlib
run pip3 install numpy


workdir /home
copy mplot_with_docker.py  mplot_with_docker.py
run chmod 777 mplot_with_docker.py

cmd python3 mplot_with_docker.py
