# -*- coding: UTF-8 -*-
import socket
import time
import ctypes
import sys
import winsound      #蜂鸣声类库

Freq = 2500
Dur  = 1000           #蜂鸣声时间

MessageBox = ctypes.windll.user32.MessageBoxA
if len(sys.argv) != 4:
    print "Usage :\n"+"\t"+sys.argv[0]+" [ip] [port][seconds]"
    exit()

ip = sys.argv[1]
port = int(sys.argv[2])
times = float(sys.argv[3])

print ip,port,times
while True:
    address = (ip,port)
    s =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        s.connect(address)
        print 'Open '
        s.close()
    except:
        print 'Close'                #目标主机对应端口未开启
        MessageBox(0,"\n\n**********Close!!!**********",  ip+":"+str(port),0)           #弹框警告（Windows基本对话框）
        winsound.Beep(Freq,Dur)         #蜂鸣声警告
        exit()
    time.sleep(times)

