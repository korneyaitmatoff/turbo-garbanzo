docker rm -f $(docker ps -aq)
docker rmi -f $(docker images -aq)

docker build . -t fastapi_lab -f api/Dockerfile_CRUD
docker build . -t reports_lab -f api/Dockerfile_REPORTS

docker compose up -d

