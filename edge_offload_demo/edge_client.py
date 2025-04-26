import socket
import pickle
import random

HOST = 'edge_server'
PORT = 9999

# Create a dummy 10x10 image with random pixel values 0-255
image = [[random.randint(0, 255) for _ in range(10)] for _ in range(10)]

print(f'[EDGE CLIENT] Image: {image}')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(pickle.dumps(image))
    data = b''
    while True:
        packet = s.recv(4096)
        if not packet:
            break
        data += packet
    count = pickle.loads(data)
    print(f'[EDGE CLIENT] Sent image. Objects detected: {count}') 