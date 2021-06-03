docker-compose build
docker login -u ${DOCKER_USR} -p ${DOCKER_PSWD}
docker-compose push