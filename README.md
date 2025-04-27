# Advances In Wireless Networks Group Project

Github: https://github.com/doylemark/advances-in-wireless-networks-group-project

Docker Hub: https://hub.docker.com/repository/docker/doylemark/awn-ubuntu 

## Sub Folders

- **nginx-html/**: Contains a custom `index.html` file used to demonstrate running an Nginx web server in Docker with a custom HTML page (our group members).
- **edge_offload_demo/**: Contains a short edge offloading demo (server and client scripts, Dockerfiles, and README) simulating an edge AI inference scenario, where a client offloads a dummy image to an edge server for simple processing.



# Basic IPC Client/Server Demo

This demo shows a simple inter-process communication (IPC) scenario using Python sockets between two Docker containers, relevant for demonstrating container networking and offloading in modern systems.

## What It Does
- **ipc_server.py**: Listens for a connection, receives a list of numbers from the client, computes the mean, median, and standard deviation, and sends the results back to the client.
- **ipc_client.py**: Sends a list of 100 numbers to the server, receives the computed statistics, and prints them.

## How to Build and Run

1. **Build the Docker images:**
   - For the server:
     ```sh
     docker build -t my_ipc_server -f Dockerfile .
     ```
   - For the client:
     ```sh
     docker build -t my_ipc_client -f Dockerfile.client .
     ```

2. **Create a user-defined Docker network:**
   ```sh
   docker network create ipc-net
   ```

3. **Run the server (in one terminal):**
   ```sh
   docker run -it --rm --name server --network ipc-net my_ipc_server
   ```

4. **Run the client (in another terminal):**
   ```sh
   docker run -it --rm --name client --network ipc-net my_ipc_client
   ```

The server will print the received numbers and computed statistics. The client will print the numbers it sent and the statistics it received from the server.


# Edge Offloading Demo

This demo illustrates a simple edge offloading scenario relevant to future wireless networks (5G/6G, edge computing, IoT).

## What It Does
- **edge_server.py**: Acts as an edge server that listens for a connection from a client, receives a dummy "image" (a 10x10 2D array of pixel values), counts the number of pixels above a threshold (simulating object detection), and returns the count to the client.
- **edge_client.py**: Acts as a client that generates a random 10x10 image, sends it to the edge server, and prints the number of detected "objects" (pixels above threshold) received from the server.

## Why This Is Relevant
Offloading computation from devices to edge servers is a key use case in advanced wireless networks. This demo simulates a basic version of edge AI inference offloading, where a device sends data to an edge node for processing, reducing device workload and latency.

## How to Build and Run

*From `./edge_offload_demo/`*

1. **Build the Docker images:**
   ```sh
   docker build -t edge_server -f Dockerfile.server .
   docker build -t edge_client -f Dockerfile.client .
   ```

2. **Create a user-defined Docker network:**
   ```sh
   docker network create edge-offload-net
   ```

3. **Run the edge server (in one terminal):**
   ```sh
   docker run -it --rm --name edge_server --network edge-offload-net edge_server
   ```

4. **Run the edge client (in another terminal):**
   ```sh
   docker run -it --rm --name edge_client --network edge-offload-net edge_client
   ```

The server will print how many objects (pixels above threshold) it detected, and the client will print the result it received from the server.
