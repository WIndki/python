import socket
import time
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(("127.0.0.1", 5005))
# 接收欢迎消息:
for data in ["TEST1","TEST2","TEST3"]:
    # 发送数据:
    data = data.encode('utf-8')
    s.send(data)
    time.sleep(1)
    print(s.recv(512).decode("utf-8"))
s.send(b"exit()")
s.close()