import socket
__IP__ = "127.0.0.1"
__PORT__ = 5005

def UDP_Send(socket,datas):
    for data in datas:
        data = data.encode('utf-8')
        socket.sendto(data,(__IP__,__PORT__))
    return

def UDP_Recv(socket):
    while(True):
        data,address = socket.recvfrom(1024)
        data = data.decode('utf-8')
        print(f"从{address}接收到{data}")

def main():
    UDP_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    select = input("选择运行模式 1 发送 2 接收")
    if select == "1":
        UDP_socket.bind((__IP__,__PORT__+1))
        UDP_Send(UDP_socket,["TEST1","TEST2","TEST3"])
    elif select == "2":
        UDP_socket.bind((__IP__,__PORT__))
        UDP_Recv(UDP_socket)
    else:
        print("error")
if __name__ == "__main__":
    main()