import threading
import socket
alias = input('Choose an alias >>> ')
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 59000)) # 127.0.0.1 = Server IP  |  59000 = Server Port

def client_receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8') # recieve "alias?"
            if message == "alias?":
                client.send(alias.encode('utf-8')) # send the alias
            else:
                print(message)
        except:
            print('Error!')
            client.close()
            break


def client_send():
    while True:
        message = f'{alias}: {input("")}' # now the client try to send a message
        client.send(message.encode('utf-8'))


receive_thread = threading.Thread(target=client_receive)
receive_thread.start()
send_thread = threading.Thread(target=client_send)
send_thread.start()