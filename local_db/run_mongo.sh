FILE=docker-compose.mongo.yml
docker-compose -f $FILE down
docker-compose -f $FILE build
docker-compose -f $FILE up
