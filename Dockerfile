FROM python:3.9.10-slim

ADD ../.. /opt/
WORKDIR /opt/

RUN export LC_ALL="en_US.UTF-8"
RUN export LC_CTYPE="en_US.UTF-8"

RUN apt-get update

RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt

RUN echo 'alias python="python3"' >> ~/.bashrc
RUN echo 'alias pip="pip3"' >> ~/.bashrc

RUN ["chmod", "+x", "./docker-entrypoint.sh"]
