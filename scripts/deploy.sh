#!/bin/bash

ssh docker-manager /bin/bash << "EOF"
export DATABASE_URI="$DATABASE_URI"
echo $DATABASE_URI
export SECRET="${SECRET}"
echo ${SECRET}
sudo docker stack deploy --compose-file docker-compose.yaml app
EOF