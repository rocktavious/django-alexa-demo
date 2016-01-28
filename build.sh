image_id=`docker-compose build alexa`
docker tag -f ${image_id: -12} rockmans/alexa:master
docker push rockmans/alexa:master
