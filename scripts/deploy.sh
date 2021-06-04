#!/bin/bash

ssh docker-manager 'export DATABASE_URI='$DATABASE_URI''
ssh docker-manager 'export SECRET='$SECRET''
ssh docker-manager "sudo docker stack deploy --compose-file docker-compose.yaml app"