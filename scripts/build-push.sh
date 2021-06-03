docker-compose build
docker login -u $DOCKER_LOGIN -p $DOCKER_PASSWORD
docker-compose push