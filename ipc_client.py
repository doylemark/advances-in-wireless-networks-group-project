import socket
import pickle

HOST = 'server'  # Use 'server' as the hostname when running in Docker network, or 'localhost' if running on host
PORT = 9898

# Generate 50+ numbers
numbers = list(range(1, 101))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(pickle.dumps(numbers))
    data = b''
    while True:
        packet = s.recv(4096)
        if not packet:
            break
        data += packet
    results = pickle.loads(data)
    print(f"[CLIENT] Sent numbers: {numbers}")
    print(f"[CLIENT] Received stats: {results}") 