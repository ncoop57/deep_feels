FROM ubuntu:latest

RUN apt update && apt upgrade -y
RUN apt install -y python3
RUN apt install -y python3-pip

WORKDIR /home/deep_feels

ADD ./deep_feels /home/deep_feels

EXPOSE 80

RUN bash setup.sh
CMD sleep infinity
CMD python3 deep_feels.py
