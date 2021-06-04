#!/bin/bash

ssh docker-manager /bin/bash << "EOF"
sudo export DATABASE_URI=$DATABASE_URI
sudo export SECRET=$SECRET
sudo docker stack deploy --compose-file docker-compose.yaml app
EOF