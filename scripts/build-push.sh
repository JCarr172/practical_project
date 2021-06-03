docker-compose build
docker login -u ${docker-hub-credentials_USR} -p ${docker-hub-credentials_PSW}
docker-compose push