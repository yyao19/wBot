# README #

WECHAT BOT

## What is this repository for? ##

* Automated Operation of Personal WeChat Account
* Version 1.0

## How do I get set up? ##

### INSTALL PYTHON 2.7 ###
Use the following guide to install Python 2.7.x on centos:
https://www.digitalocean.com/community/tutorials/how-to-set-up-python-2-7-6-and-3-3-3-on-centos-6-4

### MAKE VIRTUALENV ###
 - pip install virtualenv
 - virtualenv wBot

### INSTALL OTHER DEPENDENCIES ###
 - cd wBot
 - source bin/activate
 - pip install package_name && pip freeze > requirements.txt
 - pip install -r requirements.txt

### Make sure before running you ###
 - set the configurations in src/config.py

=== USER RUN GUIDE ===
 TO RUN:
 $> source bin/activate
 $> python wBot.py