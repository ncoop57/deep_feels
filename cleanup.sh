#! /bin/bash

docker stop $(sudo docker ps -a -q)

docker rm $(sudo docker ps -a -q)

docker rmi -f $(sudo docker images -aq)
