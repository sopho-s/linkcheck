FROM ubuntu:latest
WORKDIR /home/ubuntu

RUN apt update
RUN apt install -y python3-pip
RUN pip3 install --break-system-packages mitmproxy


RUN ls ~/.mitmproxy/

RUN cd ~/.mitmproxy
RUN python3 -m http.server 8888