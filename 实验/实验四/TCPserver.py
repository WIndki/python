import socket
import threading
import time
__IP__ = "127.0.0.1"
__PORT__ = 5005

def reply_message(socket_input,address):
    print(f"来自{address}的TCP")
    while(True):
        input_data = socket_input.recv(512).decode("utf-8")
        time.sleep(1)#等待
        print(f"从{address}接受到:{input_data}")
        if not input_data or input_data == "exit()":
            break
        socket_input.send((f"收到:{input_data}").encode("utf-8"))
    socket_input.close()
    print(f"来自{address}的TCP已关闭")

def main():
    tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    tcp_socket.bind((__IP__,__PORT__))
    tcp_socket.listen(10)
    print(f"已开始监听{__IP__}:{__PORT__}")
    while(True):
        socket_input,address = tcp_socket.accept()
        thread = threading.Thread(target=reply_message,args=(socket_input,address))
        thread.start()

if __name__ == "__main__":
    main()