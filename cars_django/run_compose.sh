COMPOSE_DOCKER_CLI_BUILD=0 DOCKER_BUILDKIT=0 docker-compose up -d
sleep 10
docker exec cars_django-api-1 python manage.py migrate