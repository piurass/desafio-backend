#!/bin/bash

pip3 install flask
pip3 install flask-jwt-extended
pip3 install peewee

cd app
python3 login.py &
python3 check.py & 
python3 viagem.py &
