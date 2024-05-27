# find the latest minecraft-server.jar file from https://www.minecraft.net/en-us/download/server
FROM ubuntu:latest

RUN apt-get update && apt-get install -y openjdk-8-jre-headless wget

RUN mkdir /minecraft
WORKDIR /minecraft
RUN wget https://launcher.mojang.com/v1/objects/1b557e7b033b583cd9f66746b7a9ab1ec1673ced/server.jar -O minecraft_server.1.20.6.jar
RUN echo "eula=true" > eula.txt

CMD [ "java", "-Xmx1024M", "-Xms1024M", "-jar", "minecraft_server.1.20.6.jar", "nogui"]