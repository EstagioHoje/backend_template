FILE=docker-compose.local.yml
docker-compose -f $FILE down
docker-compose -f $FILE build
docker-compose -f $FILE up