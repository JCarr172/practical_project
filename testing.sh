
#!/bin/bash

#apt install
sudo apt-get update
sudo apt-get install python3 python3-venv python3-pip -y

#setup venv and install pip requirements
python3 -m venv venv
source venv/bin/activate
pip3 install -r code/frontend/requirements.txt


python3 -m pytest frontend 
python3 -m pytest statline-generator
python3 -m pytest race-generator
python3 -m pytest class-generator