# set the base image. Since we're running 
# a Python application a Python base image is used
FROM python:3.8
# set a key-value label for the Docker image
LABEL maintainer="rumned"
WORKDIR \Desktop\code\SwiftDevOps\nd064_course_1\ 
COPY ./techtrends/ .
RUN pip install -r requirements.txt
RUN python init_db.py
RUN pip install -r requirements.txt
EXPOSE 3111
CMD [ "python", "app.py" ]