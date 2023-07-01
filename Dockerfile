# instructions for creating a Docker image
# create a container that will run a Django web application
# and ensure that sets the container with the configs below for anyone (os doesn't matter):

# use python baseimage
FROM python:3 
# copy all of the local files to the current dir in case they change
COPY .  /usr/src/app
# cd directory
WORKDIR /usr/src/app
RUN pip install -r requirements.txt
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
# CMD ["python3", "manage.py", "migrate", "&&", "python3", "manage.py", "runserver", "0.0.0.0:8000"]

# COPY: from dir into a container and store in /usr/src/app
#       Including: requirements, manage.py, applications files, settings files, etc.
# WORKDIR: change my working dri to /usr/src/app inside of a container
# RUN: install requirements 
# CMD: command that should run when the container starts off,
#      in a form of a Python list.

# docker ps # gives docker ids
# docker build -t username/APP_NAME:1.0 . # define a name tag to an image. :1.0 is a version
# docker push # to run this image on some server


# docker run -p 5000:8080 <id> # local:container2

# ENV PORT=8080
# EXPOSE 8080

### To share data across multiple containers
# docker volume create shared-stuff
# 

### Debugging
