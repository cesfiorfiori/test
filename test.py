import socket
import threading

HOST = '127.0.0.1' 
PORT = 12345       
HEADER = 1024      


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR) 


def send_message():
    while True:
        try:
            message = input("") 
            if message.lower() == 'quit': 
                client.send("quit".encode('utf-8'))
                client.close()
                break
            else:
                full_message = f"{my_name}: {message}"
                client.send(full_message.encode('utf-8'))
        except:
            print("Error.")
            client.close()
            break

def receive_message():
    while True:
        try:
            message = client.recv(HEADER).decode('utf
