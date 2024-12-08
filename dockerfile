# base image
FROM ubuntu

# author name
MAINTAINER Ramesh

# update command
RUN apt update

# start up executable
CMD [ "echo", "This is my first Image" ]
