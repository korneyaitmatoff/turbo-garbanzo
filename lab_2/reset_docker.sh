docker rm -f $(docker ps -aq)
docker rmi -f $(docker images -aq)

docker build . -t fastapi_lab

docker compose up -d