sudo docker-compose build
sudo docker login -u ${DOCKER_USR} -p ${DOCKER_PSWD}
sudo docker-compose push