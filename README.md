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
