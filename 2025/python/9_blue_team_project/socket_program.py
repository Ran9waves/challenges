#to start listenning on a socket after running this code, run "netstat -tulnp" on a different terminal tab
#to test tCP: telnet localhost PORT displays a message from the socket server if the connection is stablished
#to test UDP: use netcat in another terminal tab: echo "Hello, UDP server" | nc -u localhost PORT

import socket

#creates a network socket using IPv4 and TCP
#socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#creates a socket server that listens on localhost at port 65432

HOST, PORT = '127.0.0.1', 65432

#to listen to the socket with TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()

#with conn:
    print("Connected:", addr)
    conn.sendall(b'TCP socket server is up and running')

# to listen to the socket with UDP
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    print(f"UDP socket server listening on {HOST}:{PORT}")
    while True:
        data, addr = s.recvfrom(1024)  # buffer size is 1024 bytes
        print("Received message from client:", data.decode())
        s.sendto(b'UDP socket server is up and running', addr)