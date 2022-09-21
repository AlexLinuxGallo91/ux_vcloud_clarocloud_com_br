FROM selenium/standalone-chrome:103.0

USER root
RUN mkdir /app
WORKDIR /app
COPY . .

RUN apt-get update -y
RUN apt-get install python3 pip vim -y
RUN pip3 install virtualenv
RUN virtualenv env
RUN /app/env/bin/pip3 install -r requirements.txt
EXPOSE 7900
USER seluser
