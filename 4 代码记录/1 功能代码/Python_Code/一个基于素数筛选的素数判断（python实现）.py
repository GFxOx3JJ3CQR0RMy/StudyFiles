'''
下面是一个素数筛选的python实现。
原理：基于已知素数判断当前数字是否为素数。
优点：素数判断流程优化，可以节约素数的判断时间
要求：
1.素数表要精确;
2.比max(prime)小的所有素数均要被收录在素数表中。
3.连续运行时，需要保证素数表始终满足1、2 两条。

缺点：
1.对素数表的组织要求过高;
2.连续调用时很难保证素数表的要求;
3.该算法只是一个思路，要想在现实环境下使用需要改进的地方还有好多。
'''

prime = [2]
#先定义一个素数表，并初始化一个元素数2
def isprime(num):
    '''判断素数并更新素数表
'''
    if num  <= 2:
        print "The number %d isless then 2" % (num)
        return False
    else :
        if(max(prime)*max(prime) < num):
           #如果当前素数表无法判断num是否为素数则更新素数表
            print"当前输入的数字为：%d,需要更新素数表" % num
            for k inrange(max(prime)+1,(num)):
               isprime(k)
           
            print "****", prime      
        for i in prime:
            #根据素数表判断num是否为素数
            if num % i ==0:
                print"least factor of %d is %d" % (num,i)
                returnFalse
        else :
            print "%d is prime"% (num)
            #将当前的数值更新入素数表
           prime.append(num)


for eachnum in range(100,200):
    isprime(eachnum)

l= len(prime)
print prime
print l


