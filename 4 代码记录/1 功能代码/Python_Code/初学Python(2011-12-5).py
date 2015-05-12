#!/usr/bin/python
# Filename:function.py
def sayHello():
    print 'Hello World!'

def printMax(a,b):
    if(a > b):
        print a,'is maximum'
    else:
        print b,'is maximum'

def func1(x):
    print 'x is',x
    x=2
    print 'Changed local x to',x


def say(message,times = 1):
    print message * times


def func(a,b = 5, c = 10):
    print 'a is', a, 'and b is', b, 'and c is',c

def printMax2(x,y):
    '''Prints the maximum of two numbers.

    The two values must be integers.'''
    x = int(x)
    y = int(y)
    if x > y:
        print x,'is maximum'
    else:
        print y,'is maximum'


#===========================
#printMax2(3, 5)
#print printMax2.__doc__
#*********这里字符文档的调用是双下划线
#python 把每一样东西都作为对象，这个包括上面写道的各个函数
#*********字符文档的调用方式可以通过 help()函数来查看
#**************例如本函数就可以通过 help(printMax2)查看，退出按q。
#===========================
#func(3,7)
#func(25,c=24)
#func(c=50,a=100)
#===========================
#say('Hello')
#say('World',5)
#===========================
#x=50
#func1(x)
#print 'x is still',x
#===========================
#printMax(2,6)
#===========================
#sayHello()