import socket

ip = socket.gethostbyname(socket.gethostname())
print(socket.gethostname())
print("Your IP is:"+ ip)

print('='*30)

while True:

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ip,5000))

    message = input("Please enter the message that you want to send: ")
    client.send(("From Client 1:"+message).encode('utf-8'))
   
    data = client.recv(1024)

    print(f"{ip} is sending to you this message: {data.decode('utf-8')}")
    client.close()
    print('='*30)
