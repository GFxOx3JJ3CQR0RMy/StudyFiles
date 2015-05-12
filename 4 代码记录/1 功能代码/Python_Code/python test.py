import socket,time
def getisNum():
        s.send('lookinscription\n')
        data= s.recv(2048)
    print data,'*************'
        a = data.split(' ')
        j = 0
        for i inrange(0,len(a)):
               j=j+1
               if (a[i]=='put'):
                       break
        result = int(a[j])
        return result

def getRedNum():
        s.send('look redjug\n')
        data= s.recv(1024)
    print data,'************'
        a = data.split(' ')
        j = 0
        for i inrange(0,len(a)):
               j += 1
               if (a[i]=='of'):
                       break
        result = int(a[j])
        return result

def getblueNum():
        s.send('look bluejug\n')
        data= s.recv(1024)
    print data,'************'
        a = data.split(' ')
        j = 0
        for i inrange(0,len(a)):
               j += 1
               if (a[i]=='of'):
                       break
        result = int(a[j])
        return result

def pullltobig(litname,litnum,bigname,bignum,result):
        bigbuf = 0
        s.send('get ' +litname  +'\n')
        data = s.recv(1024)
        print data
        s.send('get ' + bigname+'\n')
        data = s.recv(1024)
        print data
        j = 0
        while(1):
               j += 1
               print '***',j,'*','0/',litnum,'*',bigbuf,'/',bignum,'*',result
               s.send('fill ' + litname +'\n')
               data = s.recv(1024)
               print data
               s.send('pour ' + litname +' into '+ bigname +'\n')
               data = s.recv(1024)
               print data
               if(bignum > litnum+bigbuf):
                       bigbuf += litnum
               elif(bignum == litnum + bigbuf):
                       bigbuf =0
                       s.send('empty '+ bigname + '\n')
                       data = s.recv(1024)
                       print data
               else :
                       s.send('empty '+ bigname + '\n')
                       data = s.recv(1024)
                       print data
                       s.send('pour '+litname+' into '+bigname+'\n')
                       data = s.recv(1024)
                       print data
                       bigbuf = litnum-(bignum-bigbuf)
               if (bigbuf==result):
                       s.send('put '+ bigname +' onto scale\n')
                       data = s.recv (1024)
                       print data
                       s.send('drop '+ litname +'\n')
                       data = s.recv(1024)
                       print data
                       s.send('look \n')
                       data = s.recv (1024)
                       print data
                       return


HOST = 'diehard.shallweplayaga.me'    # The remotehost
PORT =4001             # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
data = s.recv(1024)
print data

str = 'nnnnnnenwn'
for i in str:
        s.send(i +'\n')
        data = s.recv(1024)
        print data

while True:
        isnum = getisNum()
        rednum = getRedNum()
        bluenum  =getblueNum()
        print isnum
        print rednum
        print bluenum
    if (rednum > bluenum):
        pullltobig('bluejug',bluenum,'red jug',rednum,isnum)
        elif(bluenum >rednum):
               pullltobig('red jug',rednum,'blue jug',bluenum,isnum)
        else:
               print 'ERROR'
    s.send('look \n')
    data = s.recv(2048)
    print data
        inputflag =raw_input('go which place--(end with q)---->')
        if inputflag != 'q':
               s.send(inputflag + '\n')
               data = s.recv(1024)
               print data
        else:
               break
#a = input('input******')
#while a!=0:
#        mysend()
#    kk = raw_input('towhere==')
#    print kk
#    s.send(kk + '\n')
#    a = input('input******')