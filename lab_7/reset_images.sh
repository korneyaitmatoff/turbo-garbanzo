docker rm -f $(docker ps -aq)
docker rmi -f $(docker images -aq)

docker build . -t fastapi_lab -f Dockerfile_CRUD
docker build . -t reports_lab -f Dockerfile_REPORTS
#
#docker compose up -d

