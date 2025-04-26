import socket
import pickle
import statistics

HOST = '0.0.0.0'
PORT = 9898

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"[SERVER] Listening on {HOST}:{PORT}")
    conn, addr = s.accept()
    with conn:
        print(f"[SERVER] Connected by {addr}")
        data = b''
        while True:
            packet = conn.recv(4096)
            if not packet:
                break
            data += packet
        numbers = pickle.loads(data)
        print(f"[SERVER] Received numbers: {numbers}")
        mean = statistics.mean(numbers)
        median = statistics.median(numbers)
        stdev = statistics.stdev(numbers)
        results = {'mean': mean, 'median': median, 'stdev': stdev}
        print(f"[SERVER] Computed stats: {results}")
        conn.sendall(pickle.dumps(results)) 