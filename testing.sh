
#!/bin/bash

#apt install
sudo apt-get update
sudo apt-get install python3 python3-venv python3-pip -y

#setup venv and install pip requirements
python3 -m venv venv
source venv/bin/activate
pip3 install -r frontend/requirements.txt


python3 -m pytest --cov-config=.coveragerc --pyargs frontend --cov-report term-missing --cov=app
python3 -m pytest --pyargs class-generator --cov-report term-missing --cov=app
python3 -m pytest --pyargs stats-generator --cov-report term-missing --cov=app
python3 -m pytest --pyargs calculator --cov-report term-missing --cov=app