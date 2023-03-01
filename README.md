To use the app without docker compose, you need to :
- go to the cloned directory
- create the network with the command : docker network create --driver bridge networkName
- start the mongo container (the image downloaded with the command docker pull mongo:latest) with : docker run --name containerName mongo
- build the python app with : docker build -t imageName .
- run the new image with : docker run --network natworkName --name containerName -p 5000:5000 -v $(pwd)/volumeBenefits.txt:/code/volumeBenefits.txt imageName
- you can go to localhost:5000 to see the result

To use the app with docker-compose :
- go to the cloned directory
- use this command : docker-compose up
- you can go to localhost:5000 to see the result
