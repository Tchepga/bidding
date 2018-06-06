#!/bin/bash

## This file contains things to help set up a sandbow for developing with Flask
## using tools like vagrant...

sudo yum -y  install python-setuptools
sudo apt-get update
sudo apt-get install -yq ntp git python-dev python-virtualenv postgresql libpq-dev
sudo pip install flask==0.10.1
sudo pip install freeze

