import time
def Myswap(a,i,j):
    buf  = a[i]
    a[i] = a[j]
    a[j] = buf

def reverse(a,i,j):
    while(i<j):
        Myswap(a,i,j)
        i += 1
        j -= 1

def combination(b,n,BackFun):
    num = 0
    if BackFun == None:
        print "Error Message : BackFun isNone !"
        print "\tdef BackFun(str) !"
        
    if(n < 2) :
        return

    if (type (b) ==  str):
        a = sorted(list(b))
    elif (type(b) == int):
        a = sorted(list(str(b)))
    else:
        a = sorted(b)
        
    while(True):
        BackFun(a)
        num +=1
        print 'num=' + str(num)
        i = n-2
        while (i>=0):
           if(a[i]<a[i+1]):
               break
            
            elif(i==0):
               
               return
            
            i -= 1;

        j = n - 1
        while( j > i ):
            if ( a[j] >a[i]):
               break
            j -= 1

        Myswap(a,i,j)
        reverse(a, i+1, n-1)

    

def CallBacktest(newStr):
    print newStr


a = '12345'
starttime = time.clock()
combination(a,len(a),CallBacktest)
endtime = time.clock()  
print (endtime-starttime) 