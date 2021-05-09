import socket

host=socket.gethostname()
port=9999
back_log=5
buffer_size=1024
tcp_server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
tcp_server.connect((host,port))
while True:
    list1=[1,2,3,4,5,6,7,0]
    for i in list1:
      tcp_server.sendall(str(i).encode())
      print('客户端已经发送消息')
      data=tcp_server.recv(buffer_size)
      print('收到服务端的信息',data)
tcp_server.close()
