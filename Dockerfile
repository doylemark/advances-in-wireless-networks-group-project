FROM ubuntu:latest

RUN apt-get update && apt-get install -y python3 python3-pip && rm -rf /var/lib/apt/lists/*
COPY ipc_server.py /ipc_server.py
EXPOSE 9898
ENTRYPOINT ["python3", "/ipc_server.py"] 