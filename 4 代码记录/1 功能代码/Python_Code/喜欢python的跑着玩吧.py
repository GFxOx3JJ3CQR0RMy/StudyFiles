##这是  DEF CON 2013 OMGACM3的代码，效率不行，提交不上去，喜欢Python编程的拿去跑着玩吧

## 由于涉及到网络通信，鉴于 2013-06-17  早晨比赛就结束了，所以代码有效期较短，想玩要趁早

##           通过递归  实现的   “躲避障碍物”

 import socket,time
def getcolnum(data):
    return 8
 
def getu(data):
    return 3
 
def numisc(raw, k , c  , data):
    #  (10 , 5 , 'u', data)
    #  (10,5) is 'u' ?
    startx = int(8*(raw-1))
    return (data[startx + k] == c)



def issafe(raw,col,searchrawnum,data):
    #(raw , col) is safe ?
    #out way

    if (not numisc(raw,col,' ',data)):
        return False
    if(searchrawnum == 1):
        return True
    if(issafe(raw-1,col,searchrawnum-1,data)):
        return True
    elif(col > 1 and \
      issafe(raw-1,col-1,searchrawnum-1,data)):
        return True
    elif(col < 6 and \
        issafe(raw-1,col+1,searchrawnum-1,data)):
        return True


def needleft(num,data):
    if num == 1:
        return False
    flag = issafe(9,(num-1),5,data)
    print 'need left'
    return flag


def needright(num,data):
    if num == 5:
        return False
    return issafe(9,(num+1),5,data)

def mysend(str):
        s.send(str)
        data = s.recv(10000)
        print str,data
        return data

def APlus():
    data = mysend('\n')
    unum = 3
    j = 0;
    while True:
        j += 1
        if j == 1000:
            break
        print '*******',j

        if needleft(unum,data):
            print 'movleft'
            data =mysend('l\n')
            unum = unum -1
        elif needright(unum,data):
            print 'movright'
            data =mysend('r\n')
            unum = unum +1
        else:
            data =mysend('\n')
        



HOST = 'grandprix.shallweplayaga.me'    # The remotehost
PORT = 2038              #The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))