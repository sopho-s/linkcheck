FROM ubuntu:latest
WORKDIR /home/ubuntu

RUN apt update
RUN apt install -y python3-pip
RUN apt install -y python3-requests
RUN apt install -y mitmproxy
EXPOSE 1234
EXPOSE 4321

COPY ./ /home/ubuntu/
RUN chmod +x /home/ubuntu/start.sh
ENTRYPOINT ["/home/ubuntu/start.sh"]