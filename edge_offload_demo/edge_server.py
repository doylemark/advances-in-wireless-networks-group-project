import socket
import pickle

HOST = '0.0.0.0'
PORT = 9999
THRESHOLD = 128

# This is a mock server that will receive an image and count the number of objects above a threshold

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print('[EDGE SERVER] Waiting for image...')
    conn, _ = s.accept()
    with conn:
        data = b''
        while True:
            packet = conn.recv(4096)
            if not packet:
                break
            data += packet
        image = pickle.loads(data)
        count = sum(1 for row in image for px in row if px > THRESHOLD)
        print(f'[EDGE SERVER] Objects detected: {count}')
        conn.sendall(pickle.dumps(count)) 