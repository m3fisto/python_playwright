# This is a poc python project


1. Create the image from the dockerfile:
docker build -t html-poc .   

2. Run the container in Docker 
docker run -dit --name my-running-app -p 8080:80 html-poc