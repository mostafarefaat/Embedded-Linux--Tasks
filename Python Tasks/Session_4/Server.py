import socket
import threading
from time import sleep

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = socket.gethostbyname(socket.gethostname())
print(socket.gethostname())
print("Your IP is:"+ ip)
print('='*30)

sock.bind((ip, 5000))
sock.listen(5)

def client_1():
    while True:
        client, addr = sock.accept() #waiting
        data = client.recv(1024)
        print(f"{addr} is sending to you (T1) this message: {data.decode('utf-8')}")
        message = input("Please enter the message that you want to send: ")
        print('='*30)
        client.send(message.encode('utf-8'))
        client.close()
        sleep(1)

def client_2():
    while True:
        client, addr = sock.accept() #waiting
        data = client.recv(1024)
        print(f"{addr} is sending to you (T2) this message: {data.decode('utf-8')}")
        message = input("Please enter the message that you want to send: ")
        print('='*30)
        client.send(message.encode('utf-8'))
        client.close()
        sleep(1)

if __name__ == '__main__':

    thread_1 = threading.Thread(target=client_1)
    thread_2 = threading.Thread(target=client_2)
    thread_1.start()
    thread_2.start()
    thread_1.join()
    thread_2.join()

    print("Done")






    

    
    