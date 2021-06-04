#!/bin/bash

'''ssh docker-manger << "EOF"
sudo export DATABASE_URI=${DATABASE_URI}
sudo export SECRET=${SECRET}
sudo docker stack depoly --compose-file docker-compose.yaml app
EOF'''