# -*- coding: UTF8 -*-
#/usr/bin/python
#Filename: test.py

import datetime
import time
# 1)判断给定正整数是否为素数。
def mysqrt(num):
    '''这个函数实现的功能是求num 的平方根的整数值

    本来用math 模块的sqrt就能完成这个功能甚至更好，
    但是，简单的功能最好还是自己实现一下吧!~~~ '''
    result = 1
    for i in range(2,num):
        if (i * i <= num):
            result = i
        else:
            break
        
    return result
def fun1(num):
    '''此函数的功能是实现：确定num是否为素数'''
    result = True
    # 下面的 for 循环使用了上面实现的mysqrt()方法
    #       效果还不错
    for i in range(2,mysqrt(num)+1):
        if(num % i == 0):
            result = False
            break
    return result


# 2)判断给定年份是否为闰年。

def fun2(year):
    '''如果year 是闰年 则返回True 否则 返回False'''
    return ((year % 4 == 0)\
            and (year % 100 !=0))\
            or (year % 400 ==0)
    

# 3)对给定正整数数列进行由大到小排序。
def fun3():
    '''这个函数的功能是：指导用户顺序输入 正整数序列然后
        从大到小排序
    '''
    h = []
    i= int(raw_input("请输入准备排序数列的第一个数字："))
    while(i != -1):
        h.append(i)
        i=int(raw_input("请输入下一个数字(-1结束)："))
    h.sort(None,None,True)
    print h
# 4)打印杨辉三角。

def fun4_1(h):
    '''此函数功能是：给定杨辉三角第i行的列表h

    计算其下一行列表 并返回'''
    n = len(h)
    h.append(0)
    h_next = []
    h_next.append(1)
    for i in range(n):
        h_next.append(h[i] + h[i+1])
    return h_next
        
def fun4(col):
    '''此函数传入一个行号用于确定要打印的杨辉三角的行数，

      随后在函数内完成打印杨辉三角的功能'''
    h = [1]
    i=0
    while(i < col):
        print h
        h = fun4_1(h)
        i = i + 1
# 5)分别统计给定字符串中字母、数字、空格及特殊字符的个数。
def fun5():
    '''首先指导用户输入一串要分析的字符串，然后输出分析结果
    '''
    h=raw_input("Please write somethinghere:")
    n = len(h)
    i = 0
    numNum = 0      #数字 计数
    charNum = 0     #字符 计数
    spaceNum = 0    #空格 计数
    specialNum = 0  #特殊 计数
    while(i<n):
        if(h[i]>='0' andh[i]<='9'):
            numNum = numNum +1
        elif((h[i] >= 'a' and h[i]<= 'z') or (h[i]>='A' and h[i] <= 'Z')):
            charNum = charNum +1
        elif(h[i] == ' '):
            spaceNum = spaceNum+ 1
        else:
            specialNum =specialNum + 1
        i = i + 1
    print 'The number of letters is    :',charNum
    print 'The number of numbers is    :',numNum
    print 'The number of space is      :',spaceNum
    print 'The number of specia_lcharis:',specialNum