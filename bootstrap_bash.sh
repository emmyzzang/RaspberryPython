#!/bin/sh

HOME=/home/pi

# baseline update / tools
sudo apt-get -y update
sudo apt-get -y upgrade

# ssh key

# python / git
sudo apt-get -y install python-setuptools python-dev git 
sudo easy_install pip

# virtualenv
sudo pip install virtualenvwrapper wiringpi wiringpi2
mkdir $HOME/Devel
mkdir $HOME/.virtualenvs 