import socket

tcp_server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostname()
port=9999
back_log=5
buffer_size=1024
tcp_server.bind((host,port))
tcp_server.listen(back_log)
while  True:
    conn,addr=tcp_server.accept()
    print('这是双向链接呢',conn)
    print('客户端地址',addr)
    while True:
        data=conn.recv(buffer_size)
        if data :
           print('客户端发来的信息',data)
           conn.send(data.upper())
        else:
            break

tcp_server.close()
