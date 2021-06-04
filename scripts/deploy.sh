#!/bin/bash

ssh docker-manager << EOF
export DATABASE_URI=${DATABASE_URI}
export SECRET=${SECRET}
docker stack deploy --compose-file docker-compose.yaml app
EOF