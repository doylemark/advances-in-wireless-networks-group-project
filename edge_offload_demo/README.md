# Edge Offloading Demo

This demo illustrates a simple edge offloading scenario relevant to future wireless networks (5G/6G, edge computing, IoT).

## What It Does
- **edge_server.py**: Acts as an edge server that listens for a connection from a client, receives a dummy "image" (a 10x10 2D array of pixel values), counts the number of pixels above a threshold (simulating object detection), and returns the count to the client.
- **edge_client.py**: Acts as a client that generates a random 10x10 image, sends it to the edge server, and prints the number of detected "objects" (pixels above threshold) received from the server.

## Why This Is Relevant
Offloading computation from devices to edge servers is a key use case in advanced wireless networks. This demo simulates a basic version of edge AI inference offloading, where a device sends data to an edge node for processing, reducing device workload and latency.

## How to Build and Run

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
